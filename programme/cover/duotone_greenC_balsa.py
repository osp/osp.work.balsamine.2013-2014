#!/usr/bin/env python2

# Copyright (C) 2011: Simeon Voelkel <simeon_voelkel@arcor.de>
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are 
# met:
#
# 1. Redistributions of source code must retain the above copyright 
#    notice, this list of conditions and the following disclaimer.
#
# 2. The name of the author may not be used to endorse or promote 
#    products derived from this software without specific prior written 
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR 
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING 
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.

import Image
import sys
from optparse import OptionParser
#import optparse

epsprolog_text="""%%Creator: duotoner.py
%%LanguageLevel: 3
%%DocumentProcessColors: Black
"""
HKS43K_text="""%%DocumentCustomColors: 
%%+ (HKS 43 K)
%%CMYKCustomColor: 
%%+ 0.94902 0.8 0 0 (HKS 43 K)
"""

HKS15K_text="""%%DocumentCustomColors: 
%%+ (HKS 15 K)
%%CMYKCustomColor: 
%%+ 0.05 1.0 0.8 0 (HKS 15 K)
"""

PANTONE_GREEN_U_text="""%%DocumentCustomColors: 
%%+ (Pantone_Green-C)
%%CMYKCustomColor: 
%%+ 1. 0 0.65 0 (Pantone_Green-C)
"""

PANTONE_GREEN_U_colorspace="""
[ /DeviceN
  [ (Pantone_Green-C) /Black ]
  /DeviceCMYK
    {
      exch
      dup 1.0 mul exch
      dup 0 mul exch
      dup 0.65 mul exch
      0 mul
      5 -1 roll
      add
   }
] setcolorspace
"""

HKS43K_colorspace="""
[ /DeviceN
  [ (HKS 43 K) /Black ]
  /DeviceCMYK
    {
      exch
      dup 0.94902 mul exch
      dup 0.8 mul exch
      dup 0.0 mul exch
      0.0 mul
      5 -1 roll
      add
   }
] setcolorspace
"""

HKS15K_colorspace="""
[ /DeviceN
  [ (HKS 15 K) /Black ]
  /DeviceCMYK
    {
      exch
      dup 0.05 mul exch
      dup 1.0 mul exch
      dup 0.8 mul exch
      0.0 mul
      5 -1 roll
      add
   }
] setcolorspace
"""

def epsprolog(ofile, width, height):
        ofile.write( '%!PS-Adobe-3.0 EPSF-3.0\n' )
        # one point (1/72 inch, unit of coord.sys) contains 25/6 dots at 300 dpi:
        ofile.write( '%%BoundingBox: 0 0 {0:f} {1:f}\n'.format((width*1), ((height+1)*1)) )
        #ofile.write( '%%BoundingBox: 0 0 {0:f} {1:f}\n'.format((width*6)/25+1, ((height+1)*6)/25+1) )
        ofile.write( '%%HiResBoundingBox: 0 0 {0:f} {1:f}\n'.format((width*1.0), ((height+1)*1.0)) )
        #ofile.write( '%%HiResBoundingBox: 0 0 {0:f} {1:f}\n'.format((width*6.0)/25.0, ((height+1)*6.0)/25.0) )
        ofile.write( epsprolog_text )
        ofile.write( PANTONE_GREEN_C_text )
        ofile.write( '%%EndComments\n' )
        ofile.write( PANTONE_GREEN_C_colorspace )
        ofile.write( '0 0 translate\n' ) 
        ofile.write( '{0:f} {1:f} scale\n'.format((width*1.0), (height*1.0)) )
        #ofile.write( '{0:f} {1:f} scale\n'.format((width*6.0)/25.0, (height*6.0)/25.0) )
        ofile.write( '<<\n' )
        ofile.write( '    /ImageType 1\n' )
        ofile.write( '    /Width {0:d}\n'.format(width) )
        ofile.write( '    /Height {0:d}\n'.format(height) )
        ofile.write( '    /BitsPerComponent 8\n' )
        ofile.write( '    /Decode [ 1 0  1 0 ]\n' )
        ofile.write( '    /ImageMatrix [ {0:d} 0 0  -{1:d} 0 {1:d} ]\n'.format(width,height) )
        ofile.write( '    /DataSource currentfile /ASCIIHexDecode filter \n' )
        ofile.write( '>>\n' )
        ofile.write( 'image\n' )

def heximageoutput(ofile,bpixel,spixel,width,height):
        for y in range(height) :
                linelength = 16;
                for x in range(width) :
                        ofile.write( '{0:02X}'.format(spixel[x,y]) )
                        ofile.write( '{0:02X}'.format(bpixel[x,y]) )
                        linelength -= 1;
                        if linelength == 0 :
                                ofile.write( '\n' )
                                linelength = 16
        ofile.write( '\n>\n' )


def epsepilog(ofile):
        ofile.write( '\n' )
        ofile.write( 'showpage\n' )
        ofile.write( '%%EOF\n' )

def do_duotone(grayimage, spotimage, epsout):
        imblack = Image.open(grayimage)
        imspot = Image.open(spotimage)
        bpixel = imblack.load()
        spixel = imspot.load()

        bwidth = imblack.size[0]
        swidth = imspot.size[0]
        bheight = imblack.size[1]
        sheight = imspot.size[1]

        bmode = imblack.mode
        smode = imspot.mode

        if bmode != 'L' :
                print('Grayscale(L) image required, but received {0:s} for black ink'.format(bmode))
                exit (-1)
        if smode != 'L' :
                print('Grayscale(L) image required, but received {0:s} for spot color'.format(smode))
                exit (-2)
        if bwidth != swidth or bheight != sheight :
                print('Image dimensions do not match!: Black: {0:d}x{1:d} vs. Spot: {2:d}x{3:d}'.format(bwidth,bheight,swidth,sheight))
                exit (-3)
        print('Image dimensions are: Black: {0:d}x{1:d} vs. Spot: {2:d}x{3:d}'.format(bwidth,bheight,swidth,sheight))

        ofile = open(epsout, 'wb')

        epsprolog(ofile,bwidth,bheight)
        heximageoutput(ofile,bpixel,spixel,bwidth,bheight)
        epsepilog(ofile)

def process_args():
        parser = OptionParser()
        parser.add_option("-b", "--black", 
                        action="store", type="string", dest="grayinfilename", default="/dev/stdin", 
                        help="image for black ink")
        parser.add_option("-s", "--spot", 
                        action="store", type="string", dest="spotinfilename", default="/dev/stdin", 
                        help="image for spot color")
        parser.add_option("-o", "--output", 
                        action="store", type="string", dest="epsoutfilename", default="/dev/stdout", 
                        help="epsfile for output")
        (options, args) = parser.parse_args()

        do_duotone(options.grayinfilename, options.spotinfilename, options.epsoutfilename)

if __name__ == "__main__":
        process_args()

