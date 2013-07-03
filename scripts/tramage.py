def tramage(image, levels):
    filename = pdb.gimp_image_get_filename(image)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.plug_in_autocrop(image, drawable)
    if levels:
        pdb.gimp_levels(drawable, 0, 5, 50, 1, 0, 255)
    pdb.plug_in_unsharp_mask(image, drawable, 5, 0.5, 0)
    try:
        pdb.plug_in_newsprint(image, drawable, 6, 0, 0, 45, 0, 0, 0, 0, 0, 0, 0, 1)
        pdb.gimp_image_convert_indexed(image, 0, 3, 2, False, True, 0)
    except: 
        pass

images = gimp.image_list()
for image in images:
    tramage(image, True)
