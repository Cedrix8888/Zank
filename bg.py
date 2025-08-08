from PIL import Image

def create_solid_color_bg(width: int = 1400,
                          height: int = 2993,
                          color: tuple = (0, 0, 0),
                          path: str = "./imgs/outputs/bg.png"):
    for value in color:
        if(value < 0 or value > 255):
            raise ValueError("RGB通道的值必须在0-255之间")
    image = Image.new('RGB', (width, height), color)
    image.save(path, 'PNG')

create_solid_color_bg(color=(0,0,41))

# Red: (255,0,0)
# Green: (0,255,0)
# Blue : (0,0,255)
# Yellow: (255,255,0)
# Cyan: (0,255,255)
# Magenta: (255,0,255)

# White: (255,255,255)
# Black: (0,0,0)
# Gray: (128,128,128)

# Purple: (128,0,128)
