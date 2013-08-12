def boost(image, ratio):
    # ratio à atteindre en pourcentage
    filename = pdb.gimp_image_get_filename(image)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_image_convert_rgb(image)
    pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.05, 0.05, 0.05, 1)
    pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.2, 0.2, 0.2, 1)
    pdb.plug_in_gauss(image, drawable, 0.5, 0.5, 1)
    height = pdb.gimp_image_height(image)
    width = pdb.gimp_image_width(image)
    pdb.gimp_context_set_interpolation(3)
    pdb.gimp_image_scale(image, width*200/100, height*200/100)
    if ratio > 200:
        pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.2, 0.2, 0.2, 1)
        height = pdb.gimp_image_height(image)
        width = pdb.gimp_image_width(image)
        pdb.gimp_image_scale(image, width*200/100, height*200/100)
        pdb.plug_in_rgb_noise(image, drawable, 1, 0, 0.2, 0.2, 0.2, 1)
    pdb.gimp_image_convert_indexed(image, 0, 3, 2, False, True, 0)

images = gimp.image_list()
for image in images:
    boost(image, 400)

