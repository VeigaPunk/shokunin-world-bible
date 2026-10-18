#!/usr/bin/env python3
"""Independent full-file digest recomputation for V61.

Does not import dependency_freeze and does not call hashlib.
Primary digest is a FIPS 180-4 SHA-256 written here. Every file is
cross-checked with `openssl dgst -sha256` (a separate implementation).
"""

import json
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
CONTRACT = LANE / "corpus/tools/dependency-freeze-contract.json"
DECLARED = (
    "entities.json",
    "relations.json",
    "timeline.json",
    "sources.json",
    "contradictions.json",
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
)

# FIPS 180-4 section 4.2.2.
K = (
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
)


def rotr(value, bits):
    return ((value >> bits) | (value << (32 - bits))) & 0xFFFFFFFF


def sha256(data):
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("sha256 expects bytes")
    state = [
        0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
        0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,
    ]
    bit_len = len(data) * 8
    padded = bytearray(data)
    padded.append(0x80)
    while (len(padded) % 64) != 56:
        padded.append(0)
    padded.extend(bit_len.to_bytes(8, "big"))
    for offset in range(0, len(padded), 64):
        block = padded[offset:offset + 64]
        words = [int.from_bytes(block[i:i + 4], "big") for i in range(0, 64, 4)]
        for index in range(16, 64):
            s0 = rotr(words[index - 15], 7) ^ rotr(words[index - 15], 18) ^ (words[index - 15] >> 3)
            s1 = rotr(words[index - 2], 17) ^ rotr(words[index - 2], 19) ^ (words[index - 2] >> 10)
            words.append((words[index - 16] + s0 + words[index - 7] + s1) & 0xFFFFFFFF)
        a, b, c, d, e, f, g, h = state
        for index in range(64):
            s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            ch = (e & f) ^ ((~e) & g & 0xFFFFFFFF)
            t1 = (h + s1 + ch + K[index] + words[index]) & 0xFFFFFFFF
            s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (s0 + maj) & 0xFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF
        state = [(left + right) & 0xFFFFFFFF for left, right in zip(state, (a, b, c, d, e, f, g, h))]
    return "".join(f"{word:08x}" for word in state)


def openssl_sha256(data):
    result = subprocess.run(
        ["openssl", "dgst", "-sha256"],
        input=data,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", "replace"))
    text = result.stdout.decode("ascii").strip()
    # "SHA2-256(stdin)= <hex>" or "SHA256(stdin)= <hex>"
    hexpart = text.split()[-1].strip().lower()
    if len(hexpart) != 64 or any(ch not in "0123456789abcdef" for ch in hexpart):
        raise RuntimeError(f"unexpected openssl output: {text!r}")
    return hexpart


def self_check():
    vectors = {
        b"": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        b"abc": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq":
            "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1",
    }
    failed = 0
    for raw, expected in vectors.items():
        got = sha256(raw)
        other = openssl_sha256(raw)
        ok = got == expected == other
        print(f"VECTOR {raw[:12]!r}... len={len(raw)} pure={got} openssl={other} expected={expected} {'ok' if ok else 'MISMATCH'}")
        if not ok:
            failed += 1
    return failed


def content_payload(digests):
    return json.dumps(digests, sort_keys=True, separators=(",", ":")).encode("utf-8")


def main():
    vector_failures = self_check()
    raw_contract = CONTRACT.read_bytes()
    contract_digest = sha256(raw_contract)
    contract_openssl = openssl_sha256(raw_contract)
    print(f"CONTRACT_BYTES {len(raw_contract)}")
    print(f"CONTRACT_SHA256_PURE {contract_digest}")
    print(f"CONTRACT_SHA256_OPENSSL {contract_openssl}")
    data = json.loads(raw_contract.decode("utf-8"))
    pins = data["pins"]
    mismatches = []
    compared = 0
    content_mismatches = []
    for name in sorted(pins):
        pin = pins[name]
        rel = pin["fixture"]
        fixture = LANE / rel
        print(f"FIXTURE {name} path={rel} exists={fixture.is_dir()} resolved={fixture.resolve()}")
        files = pin["files"]
        disk = {}
        for filename in DECLARED:
            path = fixture / filename
            if not path.is_file():
                mismatches.append(f"{name}/{filename} MISSING on disk")
                print(f"  MISSING {filename}")
                continue
            blob = path.read_bytes()
            pure = sha256(blob)
            other = openssl_sha256(blob)
            pinned = files.get(filename)
            disk[filename] = pure
            compared += 1
            status = "MATCH" if pure == other == pinned else "MISMATCH"
            print(f"  {filename} bytes={len(blob)} pure={pure} openssl={other} pin={pinned} {status}")
            if pure != other:
                mismatches.append(f"{name}/{filename} pure!=openssl {pure} != {other}")
            if pure != pinned:
                mismatches.append(f"{name}/{filename} pure!=pin {pure} != {pinned}")
            if other != pinned:
                mismatches.append(f"{name}/{filename} openssl!=pin {other} != {pinned}")
        extra = sorted(set(files) - set(DECLARED))
        missing_pin = sorted(set(DECLARED) - set(files))
        if extra or missing_pin:
            mismatches.append(f"{name} keyset extra={extra} missing={missing_pin}")
            print(f"  KEYSET extra={extra} missing_from_pin={missing_pin}")
        if len(disk) == 10:
            payload = content_payload(disk)
            pure_content = sha256(payload)
            openssl_content = openssl_sha256(payload)
            pinned_content = pin.get("content_sha256")
            status = "MATCH" if pure_content == openssl_content == pinned_content else "MISMATCH"
            print(f"  CONTENT payload_bytes={len(payload)} pure={pure_content} openssl={openssl_content} pin={pinned_content} {status}")
            print(f"  CONTENT_PAYLOAD {payload.decode('ascii')}")
            if pure_content != pinned_content or openssl_content != pinned_content or pure_content != openssl_content:
                content_mismatches.append(name)
    print(f"COMPARED {compared}")
    print(f"FILE_MISMATCHES {len(mismatches)}")
    for item in mismatches:
        print(f"MISMATCH {item}")
    print(f"CONTENT_MISMATCHES {content_mismatches}")
    print(f"VECTOR_FAILURES {vector_failures}")
    if vector_failures or mismatches or content_mismatches or compared != 60:
        print("RESULT FAIL")
        return 1
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
