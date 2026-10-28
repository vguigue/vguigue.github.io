#!/usr/bin/env python3
"""Copie les N premières news de event.md dans la section News de index.md.

Dans event.md, les news sont les paragraphes (séparés par une ligne vide)
qui suivent le premier titre d'année "### ...". Les titres et les liens
"[↑ top]" sont ignorés, et on passe à l'année précédente si besoin.

Dans index.md, le bloc remplacé est celui compris entre les marqueurs
<!-- news:start --> et <!-- news:end -->.

Usage (depuis la racine du site) :
    python3 script/update_news.py        # 3 news
    python3 script/update_news.py -n 5   # 5 news
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS = ROOT / "event.md"
INDEX = ROOT / "index.md"
START = "<!-- news:start -->"
END = "<!-- news:end -->"


def read_news(text):
    # tout ce qui précède le premier titre d'année (titre, menu) est ignoré
    match = re.search(r"^### ", text, flags=re.MULTILINE)
    if match is None:
        sys.exit("Aucun titre '### <année>' trouvé dans event.md")
    paragraphs = re.split(r"\n[ \t]*\n", text[match.start():])
    news = []
    for p in paragraphs:
        p = p.strip()
        if not p or p.startswith("#") or p.startswith("[↑"):
            continue
        news.append(p)
    return news


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-n", type=int, default=3, help="nombre de news (défaut : 3)")
    args = parser.parse_args()

    news = read_news(EVENTS.read_text(encoding="utf-8"))[: args.n]
    index = INDEX.read_text(encoding="utf-8")
    if START not in index or END not in index:
        sys.exit(f"Marqueurs {START} / {END} absents de index.md")

    before, rest = index.split(START, 1)
    _, after = rest.split(END, 1)
    block = "\n\n".join(news)
    INDEX.write_text(f"{before}{START}\n\n{block}\n\n{END}{after}", encoding="utf-8")

    print(f"{len(news)} news copiées dans index.md :")
    for p in news:
        print("  -", p.splitlines()[0][:90])


if __name__ == "__main__":
    main()
