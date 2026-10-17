import os, sys
paths = sys.argv[1:]
bad = [p for p in paths if not os.path.exists(p)]
for p in paths:
    print(("OK   " if os.path.exists(p) else "MISS "), p)
print("MISSING:", len(bad))
