#!/usr/bin/env python3

# liblintel.py - The Lintel Library.
# (c) 2025 DWNfonts.


def _locateMagicList(char):
    __MAGIC_LIST = [  # everytime I name the list/dict as magic
        "⿾⿿〾",  # IDCs followed by 1 char/IDS
        "⿰⿱⿴⿵⿶⿷⿸⿹⿺⿼⿽㇯⿻",  # IDCs followed by 2 chars/IDSs
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
        if isinstance(self.idc, str):
            return (
                f"Lintel<{ self.idc + "".join([str(x) for x in self.chars]) }+{ self.notProcessed }>"
                if self.notProcessed != ""
                else f"Lintel<{ self.idc + ''.join([str(x) for x in self.chars]) }>"
            )
        else:
            return (
                f"Lintel<{ ''.join([str(x) for x in self.chars]) }+{ self.notProcessed }>"
                if self.notProcessed != ""
                else f"Lintel<{ ''.join([str(x) for x in self.chars]) }>"
            )

    def __str__(self) -> str:
        if isinstance(self.idc, str):
            return self.idc + "".join([str(x) for x in self.chars]) + self.notProcessed
        else:
            return "".join([str(x) for x in self.chars]) + self.notProcessed


class LintelWithSource:
    def __init__(self, ids: Lintel | str, source: list) -> None:
        self.ids = ids
        self.source = source

    def __repr__(self) -> str:
        return f"LWS^{self.ids}$({"".join(self.source)})"


def importIDS(ids) -> Lintel | str:
    if len(ids) == 0:
        return ""
    firstChar = ids[0]
    loop = _locateMagicList(firstChar)
    match loop:
        case 0:
            return firstChar
        case _:
            idc = firstChar
            remainCharList = []
            remainChars = ids[1:]
            for _ in range(loop):
                lintel = importIDS(remainChars)
                if isinstance(lintel, Lintel):
                    noNotProcessed = Lintel(lintel.idc, lintel.chars)
                    remainCharList.append(noNotProcessed)
                    remainChars = (
                        lintel.notProcessed
                        if isinstance(remainCharList[-1], Lintel)
                        else remainChars[1:]
                    )
                else:
                    if lintel != "":
                        remainCharList.append(lintel)
                    remainChars = remainChars[1:]
            chars = tuple(remainCharList)
            return Lintel(idc, chars, notProcessed=remainChars)


def importIDSWithSource(idswsrc):
    import re

    MAGIC_RE = "^\\^[^ ]*\\$([^ ]*)"
    if not re.match(MAGIC_RE, idswsrc):
        raise Exception("Invalid IDS")
    else:
        idc, source = idswsrc.split("$")
        idc, source = idc[1:], source[1:-1]
        return LintelWithSource(importIDS(idc), source)


def _test():

    def _debug(text, lf=False):
        import sys

        end = "" if lf else "\n"
        print(text, file=sys.stderr, end=end)

    lws = importIDSWithSource("^⿰衤⿱𥫗灭$(GT)")
    print([lws])


# if __name__ == "__main__": _test()
