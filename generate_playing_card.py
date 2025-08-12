from gimpfu import register, main, pdb
from config import config
from layout.size import create_size

# Точка входу для GIMP, з мінімальною інтеграцією
def plugin_entry_point(width, height,suit,rank):
    config.width = width
    config.height = height
    config.suit = suit
    config.rank = rank

    # Викликаємо бізнес-логіку
    image, layer = create_canvas(config)
    # можна одразу відкрити у вікні GIMP
    gimp.Display(image)
    gimp.Displays_flush()

register(
    "python_fu_playing_card",
    "Playing Card Generator",
    "Створює шаблон гральної карти",
    "KRaN",
    "KRaN",
    "2025",
    "<Image>/Filters/Custom/Playing Card Generator",
    "",
    [
        (PF_INT, "width", "Ширина (px)", config.width),
        (PF_INT, "height", "Висота (px)", config.height),
        (PF_STRING, "suit", "Масть", config.suit),
        (PF_STRING, "rank", "Ранг", config.rank),
    ],
    [],
    plugin_entry_point
)

if __name__ == "__main__":
    main()