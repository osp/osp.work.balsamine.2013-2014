#! /usr/bin/python

"""
Usage:
    python 2fontsin1.py fonte1.ufo fonte2.ufo fonte-out.ufo
"""


import fontforge
import psMat
import math
import sys

matrix = psMat.rotate(math.radians(45))

font1 = fontforge.open(sys.argv[1])
font2 = fontforge.open(sys.argv[2])

for glyph in font1.glyphs():
    #glyph.wireframe(100, 300, -45)
    font1.selection.select(glyph.glyphname)
    font1.copy()
    font2.selection.select(glyph.glyphname)
    font2.pasteInto()
    font2.removeOverlap()

font2.generate(sys.argv[3])
