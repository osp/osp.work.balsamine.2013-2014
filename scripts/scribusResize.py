#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus as s

objets = s.getAllObjects()
ratio = 0.25

for o in objets:
    s.selectObject(o)
    s.unGroupObject()
    s.deselectAll()

objets = s.getAllObjects()

for o in objets:
    s.selectObject(o)
    size = s.getSize()
    s.sizeObject(size[0]*ratio, size[1]*ratio)
    position = s.getPosition()
    s.moveObjectAbs(position[0]*ratio, position[1]*ratio)
    stroke = s.getLineWidth()
    s.setLineWidth(stroke*ratio)
    kind = s.getObjectType()
    # TextFrame, Polygon, ImageFrame

    if kind == 'TextFrame':
        try:
            s.selectText(0, -1)
            fontsize = s.getFontSize()
            s.setFontSize(fontsize*ratio)
        
        #try:
            #lineheight = s.getLineSpacing()
            #s.setLineSpacing(lineheight*ratio)
        #s.deselectAll()
        #s.selectObject(o)
        #s.selectText(0, -1)
        except:
            pass
    if kind == 'ImageFrame':
        scale = s.getImageScale()
        s.setImageScale(scale[0]*ratio, scale[1]*ratio)
    s.deselectAll()



objets = s.getAllObjects()

for o in objets:
    s.selectObject(o)
    kind = s.getObjectType()
    if kind == 'TextFrame':
        #s.selectText(0, -1)
        lineheight = s.getLineSpacing()
        s.setLineSpacing(lineheight*ratio)
    s.deselectAll()
