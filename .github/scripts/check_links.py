"""Check every relative link and image in the Markdown files of this repository:  python3 .github/scripts/check_links.py

A link counts as broken if the file it points to does not exist, or if it points to a heading
(#anchor) that the target Markdown file does not have. External links are not fetched.
Standard library only.
"""
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LINK = re.compile(r"\]\(([^)\s]+)\)|<img[^>]*\ssrc=\"([^\"]+)\"")


def anchors(path):
    text = open(path, encoding="utf-8").read()
    out = {re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-") for h in re.findall(r"^#+ (.+)$", text, re.M)}
    out.update(re.findall(r'<a (?:name|id)="([^"]+)"', text))
    return out


def main():
    broken = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            src = os.path.join(d, f)
            for m in LINK.finditer(open(src, encoding="utf-8").read()):
                link = m.group(1) or m.group(2)
                if re.match(r"^[a-z]+:", link):
                    continue
                target, _, frag = link.partition("#")
                path = os.path.normpath(os.path.join(d, target)) if target else src
                if not os.path.exists(path):
                    broken.append((src, link, "missing file"))
                elif frag and path.endswith(".md") and frag not in anchors(path):
                    broken.append((src, link, "missing heading"))
    for src, link, why in broken:
        print(f"{os.path.relpath(src, ROOT)}: {link}  ({why})")
    print(f"{len(broken)} broken link(s)")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
