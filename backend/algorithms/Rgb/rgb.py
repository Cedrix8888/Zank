from PIL import Image
from utils.image import hex_rgb

def gen_rgb(width: int = 1400,
            height: int = 2993,
            color: str = "#000000"
            ):
    color = hex_rgb(color)
    image = Image.new("RGB", (width, height), color)
    return image
    