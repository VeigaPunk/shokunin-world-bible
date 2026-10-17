import html
import re
import urllib.request
from html.parser import HTMLParser

URL = "https://www.gutenberg.org/files/53080/53080-h/53080-h.htm"


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        if data.strip():
            self.parts.append(data)


response = urllib.request.urlopen(URL, timeout=20)
raw = response.read().decode("utf-8", "replace")
parser = Text()
parser.feed(raw)
body = re.sub(r"\s+", " ", html.unescape(" ".join(parser.parts)))
quote_at = body.find("The beginning of this interesting book is taken up with the Kiche story")
markers = list(re.finditer(r"\[\s*209\s*\]", body[:quote_at])) if quote_at >= 0 else []
checks = {
    "title": "The Myths of Mexico & Peru" in html.unescape(raw),
    "author": "Lewis Spence" in html.unescape(raw),
    "chapter_v": body.rfind("CHAPTER V", 0, quote_at) >= 0,
    "maya_heading": body.rfind("THE MAYA", 0, quote_at) >= 0,
    "printed_209_before_passage": bool(markers),
    "creation_story_heading": body.rfind("The Creation-Story", 0, quote_at) >= 0,
    "first_quoted_clause": "The beginning of this interesting book is taken up with the Kiche story of the creation" in body,
    "second_quoted_clause": "He called out “Earth,” and the solid land appeared." in body,
}
print(f"HTTP {response.status} {URL}")
for name, passed in checks.items():
    print(f"{'PASS' if passed else 'FAIL'} {name}")
print(f"nearest [209] marker offset: {markers[-1].start() if markers else 'absent'}")
if not all(checks.values()):
    raise SystemExit(1)
