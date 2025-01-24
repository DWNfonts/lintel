#!/usr/bin/env python3

# txt2lintel.py - IDS.TXT to Lintel groups.
# (c) 2025 DWNfonts.

import liblintel, io


def txt2lintelGroup(txt: str | io.TextIOWrapper):
    import sys

    result = {}
    for line in txt:
        if line.startswith("#"):
            print(f"\033[43mComment line: `{line.rstrip()}'\033[0m", file=sys.stderr)
            continue
        else:
            try:
                line = line.strip().split("\t")
                zi = line[1]
                ids = line[2:]
                for i in range(len(ids)):
                    if ids[i].startswith("*"):  # Inline comment
                        print(
                            f"\033[43mInline comment: `{"\t".join(ids[i:])}'\033[0m",
                            file=sys.stderr,
                        )
                        ids = ids[1:i]
                        break
                lintelList = [liblintel.importIDSWithSource(i) for i in ids]
                result[zi] = lintelList
            except:
                print(
                    f"\033[43mInvaild data: `{line}', skip\033[0m",
                    file=sys.stderr,
                    end="",
                )

    if txt is io.TextIOWrapper:
        txt.close()
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
