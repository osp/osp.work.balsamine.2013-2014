#à utiliser depuis la console python dans Gimp

def save_all_layers(image, directory, name_pattern):
    for layer in image.layers:
        try:
            layer.remove_mask(0)
        except: 
            pass
        filename = directory + (name_pattern % layer.name)
        raw_filename = name_pattern % layer.name
        pdb.gimp_file_save(image, layer, filename, raw_filename)

gimp.image_list()
img = gimp.image_list()[0]
save_all_layers(img, "/path/to/save/directory/", "image_%s.png")
