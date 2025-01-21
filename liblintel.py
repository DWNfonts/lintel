#!/usr/bin/env python3

# liblintel.py - The Lintel Library.
# (c) 2025 DWNfonts.


class Lintel:

    def _locateMagicList(self, char):
        __MAGIC_LIST = [  # everytime I name the list/dict as magic
            "⿾⿿〾",  # IDCs followed by 1 char/IDS
            "⿰⿱⿴⿵⿶⿷⿸⿹⿺⿼⿽㇯",  # IDCs followed by 2 chars/IDSs
            "⿲⿳",  # IDCs followed by 3 chars/IDSs
        ]
        for i in range(len(__MAGIC_LIST)):
            if char in __MAGIC_LIST:
                return i
        raise KeyError("Not an IDS in __MAGIC_LIST.")

    def __init__(self, *sequence) -> None:  # force-creating, danger as fuck
        self.idc = sequence[0]
        self.chars = sequence[1:]

    def __str__(self) -> str:
        return self.idc + "".join(self.chars)

    def fromIDS(self, ids):
        pass


def _test():

    def _debug(*text, lf=False):
        import sys

        end = "" if lf else "\n"
        print(text, file=sys.stderr, end=end)

    lintel = Lintel("1", "2", "3")
    _debug(lintel.idc)
    _debug(lintel.chars)
    _debug(str(lintel))


if __name__ == "__main__":
    _test()
