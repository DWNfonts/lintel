#!/usr/bin/env python3

# lintel-stat.py - Statistics for Lintel.
# (c) 2025 DWNfonts.

import liblintel, txt2lintel, sys


def stat(lintelGroup: dict, file=sys.stdout):
    totalChar = 0
    print(
        "# No.\tZi\tSource\tIDC\tComponent A\tComponent B, or\n# No.\tZi\tSource\tSingle\tIDC\tComponent.\n# See `docs/lintelstat.py` for more details.",
        file=file,
    )
    ziList = list(lintelGroup)
    goodEntry = ""
    for i in range(len(ziList)):
        zi = ziList[i]
        for lws in lintelGroup[zi]:
            ids = lws.ids
            source = lws.source
            if isinstance(ids, liblintel.Lintel):
                idc = ids.idc
                if idc == "〾":
                    pass  # TODO
                else:
                    if idc != "⿻":
                        chars = ids.chars
                        if len(chars) == 2:
                            if isinstance(chars[0], str) and isinstance(chars[1], str):
                                print(
                                    f"{i}\t{zi}\t{source}\t{idc}\t{"\t".join(chars)}",
                                    file=file,
                                )
                                goodEntry += zi
                            else:
                                print(
                                    f"Zi {zi} ({source}, {str(ids)}) contains sub-lintel, skip.",
                                    file=sys.stderr,
                                )
                        elif len(chars) == 1:
                            print(
                                f"{i}\t{zi}\t{source}\tSingle\t{idc}\t{chars[0]}",
                                file=file,
                            )
                            goodEntry += zi
                        else:
                            print(
                                f"Zi {zi} ({source}, {str(ids)}) contains more 3 chars, skip.",
                                file=sys.stderr,
                            )
                    else:
                        print(
                            f"Zi {zi} ({source}, {str(ids)}) contains ⿻, skip.",
                            file=sys.stderr,
                        )
    totalChar = len(set(goodEntry))
    print(f"# Total: {totalChar}/{len(ziList)}", file=file)


def _test():
    result = txt2lintel.txt2lintelGroup(open("data/IDS.TXT", encoding="utf-8"))
    with open("data/stat.txt", mode="w", encoding="utf8") as f:
        stat(result, file=f)


def _main():
    result = txt2lintel.txt2lintelGroup(sys.stdin.read())
    stat(result)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "w":
        _test()
    else:
        _main()
