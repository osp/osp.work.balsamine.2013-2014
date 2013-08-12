#! /usr/bin/python
# -*- coding: UTF-8 -*-
#from gimpfu import *



import math
def boostBitmap(image, ratio):
    # ratio à atteindre en pourcentage
    passages = int(math.ceil(ratio/200))
    filename = pdb.gimp_image_get_filename(image)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_image_convert_rgb(image)
    pdb.plug_in_hsv_noise(image, drawable, 2, 43, 7, 29)
    pdb.plug_in_hsv_noise(image, drawable, 2, 43, 7, 29)
    #pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.05, 0.05, 0.05, 1)
    #pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.2, 0.2, 0.2, 1)
    pdb.plug_in_gauss(image, drawable, 0.5, 0.5, 1)
    height = pdb.gimp_image_height(image)
    width = pdb.gimp_image_width(image)
    pdb.gimp_context_set_interpolation(3)
    pdb.gimp_image_scale(image, width*200/100, height*200/100)
    if passages > 0:
        for i in range(passages):
            pdb.plug_in_hsv_noise(image, drawable, 2, 43, 7, 29)
            #pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.2, 0.2, 0.2, 1)
            height = pdb.gimp_image_height(image)
            width = pdb.gimp_image_width(image)
            pdb.gimp_image_scale(image, width*200/100, height*200/100)
            pdb.plug_in_hsv_noise(image, drawable, 2, 43, 7, 29)
            pdb.plug_in_hsv_noise(image, drawable, 2, 43, 7, 29)
            #pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.5, 0.5, 0.5, 1)
    pdb.gimp_image_convert_indexed(image, 0, 3, 2, False, True, 0)

images = gimp.image_list()
boostBitmap(images[0], 400)

#register(
    #"python_fu_boost_bitmap",
    #"Boost by step of 200% a bitmap image",
    #"Boost by step of 200% a bitmap image",
    #"OSP (Stéphanie Vilayphiou",
    #"OSP (Stéphanie Vilayphiou)",
    #"GNU GPL 3",
    #"<Image>/Filters/Custom/Boost Bitmap",
    #"",
    #[
        #(PF_STRING, "source", "Source Image", "/home/"),
    #],
    #[],
    #boostBitmap
#)
#main()

