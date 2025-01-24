#!/usr/bin/env python3

# gui.py - Tk GUI for txt2lintel.py.
# (c) 2025 DWNfonts.

# I use Windows now, Windows always fucks up those texts.

import txt2lintel
import tkinter.filedialog, tkinter.messagebox

filename = tkinter.filedialog.askopenfilename(
    title="Select the IDS.TXT file...",
    filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
)
with open(filename, encoding="utf8") as f:
    saveas = tkinter.filedialog.asksaveasfilename(
        title="Save the JSON file as...",
        filetypes=(("JSON files", "*.json"), ("All files", "*.*")),
    )
    with open(saveas, "w", encoding="utf8") as g:
        g.write(txt2lintel.lintelGroup2json(txt2lintel.txt2lintelGroup(f)))
        tkinter.messagebox.showinfo("Complete", "Converted to JSON successfully!")
