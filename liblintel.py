#!/usr/bin/env python3

# liblintel.py - The Lintel Library.
# (c) 2025 DWNfonts.


def _locateMagicList(char):
    __MAGIC_LIST = [  # everytime I name the list/dict as magic
        "⿾⿿〾",  # IDCs followed by 1 char/IDS
        "⿰⿱⿴⿵⿶⿷⿸⿹⿺⿼⿽㇯",  # IDCs followed by 2 chars/IDSs
        "⿲⿳",  # IDCs followed by 3 chars/IDSs
    ]
    for i in range(len(__MAGIC_LIST)):
        if char in __MAGIC_LIST[i]:
            return i + 1
    return 0


class Lintel:

    def __init__(
        self, idc: None | str, chars: tuple, notProcessed=""
    ) -> None:  # force-creating, danger as fuck
        self.idc = idc
        self.chars = chars
        self.notProcessed = notProcessed

    def __repr__(self) -> str:
        if self.idc is str:
            return f"Lintel<{ self.idc + "".join([str(x) for x in self.chars]) }+{ self.notProcessed }>"
        else:
            return f"Lintel<{ ''.join([str(x) for x in self.chars]) }+{ self.notProcessed }>"

    def __str__(self) -> str:
        if self.idc is str:
            return self.idc + "".join([str(x) for x in self.chars]) + self.notProcessed
        else:
            return "".join([str(x) for x in self.chars]) + self.notProcessed


def importIDS(ids) -> Lintel:
    firstChar = ids[0]
    loop = _locateMagicList(firstChar)
    match loop:
        case 0:
            idc = None
            # todo: {#}
            chars = tuple(firstChar)
            notProcessed = ids[1:]
        case _:
            idc = firstChar
            remainCharList = []
            remainChars = ids[1:]
            for _ in range(loop):
                remainCharList.append(importIDS(remainChars))
                remainChars = remainCharList[-1].notProcessed
            chars = tuple(remainCharList)
            notProcessed = remainChars
    return Lintel(idc, chars, notProcessed=notProcessed)


def _test():

    def _debug(text, lf=False):
        import sys

        end = "" if lf else "\n"
        print(text, file=sys.stderr, end=end)

    lintel = importIDS("⿺辶⿳穴⿲月⿱⿲幺言幺⿲長馬長刂心")
    _debug(lintel)
    _debug(lintel.idc)
    _debug(lintel.chars)


# if __name__ == "__main__": _test()
