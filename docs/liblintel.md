# Documents of `liblintel.py` - The Lintel Library.
[< Back](./README.md)

My ability to write the document is close to shit. If you cannot read, following the following step.
 1. Don't mind to use an LLM, but I recommend *NOT TO USE IT*, so you'd better ...
 2. [Contact me.](../README.md#contact-me)

As I said, Lintel is also a replacement of the "Ideographic Description Sequence", or IDS.

## Directly new a Lintel object

```python
def __init__(
    self, idc: None | str, chars: tuple, notProcessed=""
) -> None: # ...
```

This can be an IDS *but* this *can* easily be a Cthulhu Mythos if you just fucking don't know anything about IDS.

[Read the fucking Wikipedia.](https://en.wikipedia.org/wiki/Chinese_character_description_languages#Ideographic_Description_Sequences) The shits in the tables are IDC. Outside the Hanzi/Kanji/Hanja or Kanji-like shit is a `char`, `chars` is a tuple of `char`s.

`self.idc`, `self.chars` and `self.notProcessed` are what you input.

The `__repr__` is a *ֆքɛƈɨǟʟ* `Lintel<processedIDS+unprocessedIDS>` pattern. The `__str__` is just what you import in `importIDS()` (wait what is this fucking function?).

When you're giving more than 2 IDC/chars, only the *first* char will be processed, and the rest will be stored in `notProcessed`. Defaule to `""`. See below so you will think it meaningful:

## `importIDS(ids: str)` - Import from an IDS string.

~~Here is the fucking function.~~

```python
lintel = liblintel.importIDS("⿰纟工迪") # Do you know? 红迪 means Reddit in Chinese. However, Reddit sucks.
# returns Lintel<⿰纟工+迪>.
```