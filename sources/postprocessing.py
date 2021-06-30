#!/usr/bin/env python3
"""Fix the font names for the variable fonts"""
# TODO (M Foley) this shouldn't be required. Send fix to fontmake
from fontTools.ttLib import TTFont
from glob import glob
import os

font_paths = glob("fonts/variable/*.ttf")

for path in font_paths:
    font = TTFont(path)
    if "Italic" in str(path):
        font["name"].setName("League Gothic", 1, 3, 1, 1033)
        font["name"].setName("Italic", 2, 3, 1, 1033)
        font["OS/2"].fsSelection = 0x0081
        font["head"].macStyle = 0x0002
        font.save(path + ".fix")
