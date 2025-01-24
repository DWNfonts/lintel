# Documents of `txt2lintel.py` - Converting BabelStone's `IDS.TXT` to a specific format (Python `dict` & JSON), with
# Documents of `gui.py` - A great utility for Windows
[< Back](./README.md)

## `txt2lintel.txt2lintelGroup()` - Convert `IDS.TXT` to Python dict.

```python
def txt2lintelGroup(txt: str | io.TextIOWrapper, lookup: list = []): # ...
```

`txt` is the **full text** of `IDS.TXT` or what `open("IDS.TXT")` returns.

`lookup` is a list of chars from `{1}` to `{n-1}`, can also be a string. **There's no two chars in one item.**

## `txt2lintel.lintelGroup2json()` - Convert the fucking group to JSON.

```python
def lintelGroup2json(lintelGroup: dict): # ...
```

Converting to JSON. Due to `__str__` cannot be **REAL** LWS, so it sucks, I think the only way is reading through your eyes™.

## `txt2lintel._main()` - How to use it?

```bash
txt2lintel.py < data/IDS.TXT > data/ids.json
```

Simple and stupid. Notice that Microsoft replace almost all chars to `?`, so here is...

## `gui.py` - Tk (fake-)GUI for `txt2lintel.py`

To use it, follow the two dialogs. And the script pull some shits to `stderr` (`txt2lintel`'s fault). Then got a message box showing it's complete. I never master GUI-design.