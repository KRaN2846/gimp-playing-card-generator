from gimpfu import pdb

# Робота з GIMP API(створення полотна)
def create_canvas(cfg):
    image = pdb.gimp_image_new(cfg.width, cfg.height, RGB)
    layer = pdb.gimp_layer_new(image, cfg.width, cfg.height, RGB_IMAGE, "Background", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(image, layer, None, 0)
    pdb.gimp_context_set_background(cfg.background_color)
    pdb.gimp.drawable_fill(layer, BACKROUND_FILL)
    return image, layer