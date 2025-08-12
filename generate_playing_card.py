from gimpfu import *

def generate_playing_card(width, height, margin, border_thickness, corner_radius, rank, suit, font, font_size):
    # colors of ranks
    red_suits = ["♥", "♦"]
    # hearts= чірва, clubs=хрестя, diamonds=бубна, spades=піка
    suit_symbols = {'hearts':"♥",'clubs': "♣",'diamonds': "♦",'spades': "♠"}
    suit_symbol = suit_symbols.get(suit, "?")
    text_color = (255, 0, 0) if suit_symbol in red_suits else (0, 0, 0)

    # Image creation
    image = gimp.Image(width, height, RGB)
    background = gimp.Layer(image, "Background", width, height, RGB_IMAGE, 100, NORMAL_MODE)
    pdb.gimp_drawable_fill(background, BACKGROUND_FILL)
    image.add_layer(background, 0)

    # Adding a frame layer
    border_layer = gimp