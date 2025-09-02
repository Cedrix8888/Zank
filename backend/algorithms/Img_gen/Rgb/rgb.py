from PIL import Image
from utils.image import hex_rgb

def gen_rgb(width: int = 1400,
            height: int = 2993,
            color_hex: str = "#000000"
            ):
    color_rgb = hex_rgb(color_hex)
    image = Image.new("RGB", (width, height), color_rgb)
    return image
    