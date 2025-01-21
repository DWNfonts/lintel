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
            if char in __MAGIC_LIST[i]:
                return i + 1
        return 0

    def __init__(
        self, *sequence, notProcessed=""
    ) -> None:  # force-creating, danger as fuck
        self.idc = sequence[0] if len(sequence) > 0 else ""
        self.chars = sequence[1:]
        self.notProcessed = notProcessed

    def fromIDS(self, ids):
        firstChar = ids[0]
        loop = self._locateMagicList(firstChar)
        match loop:
            case -1:
                # todo: {#}
                self.chars = tuple(firstChar)
                self.notProcessed = ids[1:]
            case _:
                remainCharList = []
                remainChars = ids[1:]
                for _ in range(loop):
                    remainCharList.append(Lintel(remainChars))
                    remainChars = remainCharList[-1].notProcessed
                    self.idc = firstChar
                print(remainCharList, remainChars)
                self.chars = tuple(remainCharList)
                self.notProcessed = remainChars

    def __str__(self) -> str:
        return self.idc + "".join(str(i) for i in self.chars)


def _test():

    def _debug(text, lf=False):
        import sys

        end = "" if lf else "\n"
        print(text, file=sys.stderr, end=end)

    lintel = Lintel("1", "2", "3")
    _debug(lintel.idc)
    _debug(lintel.chars)
    _debug(str(lintel))

    lintel = Lintel()
    lintel.fromIDS("⿱僃心")
    _debug(lintel.idc)
    _debug(lintel.chars)
    _debug(str(lintel))


if __name__ == "__main__":
    _test()
