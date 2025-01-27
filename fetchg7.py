#!/usr/bin/env python3

# fetchg7.py - Fetch some charsets from zi.tools and system.
# (c) 2025 DWNfonts.

# This script requires `requests` to load.

import requests
import sys

sys.stdout.reconfigure(encoding="utf-8")


def fetchg7():
    # Fetch the charset from zi.tools.
    r = requests.get("https://zi.tools/api/ma/ma/g7.json")
    zt_g7 = r.json()
    g7 = [x[1] for x in zt_g7["rows"]]
    return g7


def fetchgcy():
    # Fetch the charset from zi.tools.
    r = requests.get("https://zi.tools/api/ma/ma/g_cy.json")
    zt_gcy = r.json()
    gcy = [x[1] for x in zt_gcy["rows"]]
    return gcy


def fetchgtg(maxchar=8105):
    # Fetch the charset from zi.tools.
    r = requests.get("https://zi.tools/api/ma/ma/g_tg.json")
    zt_gtg = r.json()
    gtg = []
    for i in range(len(zt_gtg["rows"])):
        id = zt_gtg["rows"][i][0]
        zi = zt_gtg["rows"][i][1]
        try:
            if int(id) <= maxchar:
                gtg.append(zi)
        except:
            pass
    return gtg


def fetchg0(lvl1=False):
    # Fetch the charset from zi.tools.
    r = requests.get("https://zi.tools/api/ma/ma/g0.json")
    zt_gcy = r.json()
    gcy = [x[1] for x in zt_gcy["rows"]]
    return gcy[:3755] if lvl1 else gcy


def allchr():
    return set(fetchg0() + fetchg7() + fetchgtg())


if __name__ == "__main__":
    result = list(allchr())
    result.sort()
    with open("data/stat.txt", encoding="utf8") as f:
        stat = []
        for lines in f:
            try:
                zi = lines.strip().split("\t")[1]
                id = lines.strip().split("\t")[0]
            except:
                zi = ""
                id = -1
            if zi in result:
                print(lines, end="")
                stat.append(id)
        print("# "+str(len(set(stat)) - 1))
