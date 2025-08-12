from dataclasses import dataclass, field

@dataclass
class CardConfig:
    # початкові і дефолтні значення
    width: int = 1280 #px
    height: int = 1980
    dpi: int
    background_color: tuple[int, int, int] = (255, 255, 255)  # RGB
    suit: str
    rank: str
    font_name: str
    font_size: int
    assert_path: str = "assets"

# Глобальний екземпляр конфігурації
config: CardConfig = CardConfig()