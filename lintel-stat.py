#!/usr/bin/env python3

# lintel-stat.py - Statistics for Lintel.
# (c) 2025 DWNfonts.

import liblintel, txt2lintel


def stat(lintelGroup: dict):
    import sys

    for zi in lintelGroup:
        for lws in lintelGroup[zi]:
            ids = lws.ids
            source = lws.source
            if isinstance(ids, liblintel.Lintel) and len(ids.chars) != 2:
                print(
                    f"{ids} has {len(ids.chars)} chars, skip",
                )


def _test():
    result = txt2lintel.txt2lintelGroup(open("data/IDS.TXT", encoding="utf-8"))
    print(stat(result))


if __name__ == "__main__":
    _test()
