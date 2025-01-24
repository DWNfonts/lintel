#!/usr/bin/env python3

# txt2lintel.py - IDS.TXT to Lintel groups.
# (c) 2025 DWNfonts.

import liblintel, io


def txt2lintelGroup(txt: str | io.TextIOWrapper, lookup: dict = {}):
    import sys, re

    def _lookup(value):
        try:
            return lookup[value]
        except:
            return ""

    result = {}
    for line in txt:
        if line.startswith("#"):
            print(f"Comment line: `{line.rstrip()}'", file=sys.stderr)
            continue
        else:
            try:
                lineText = line.strip()
                unencoded = re.findall("\\{(.*?)\\}", lineText)
                if len(unencoded) > 0:
                    for i in [int(x) - 1 for x in unencoded]:
                        data = _lookup(i)
                        lineText = lineText.replace(f"{{{i}}}", data)
                        pass
                line = lineText.split("\t")
                zi = line[1]
                ids = line[2:]
                for i in range(len(ids)):
                    if ids[i].startswith("*"):  # Inline comment
                        print(
                            f"Inline comment: `{"\t".join(ids[i:])}'",
                            file=sys.stderr,
                        )
                        ids = ids[1:i]
                        break
                lintelList = [liblintel.importIDSWithSource(i) for i in ids]
                result[zi] = lintelList
            except:
                print(
                    f"Invaild data: `{line}', skip",
                    file=sys.stderr,
                )
    return result


def lintelGroup2json(lintelGroup: dict):
    import json

    result = {}
    for zi in lintelGroup:
        result[zi] = [str(i) for i in lintelGroup[zi]]
    return json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False)


def _main():
    import sys

    txt = sys.stdin.read()
    result = txt2lintelGroup(txt)
    print(lintelGroup2json(result))


if __name__ == "__main__":
    _main()
