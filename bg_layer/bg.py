from PIL import Image

def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c * 2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_solid_color_bg(width: int = 1400,
                          height: int = 2993,
                          color: tuple = (0, 0, 0)
                          ):
    for value in color:
        if(value < 0 or value > 255):
            raise ValueError("RGB通道的值必须在0-255之间")
    image = Image.new('RGB', (width, height), color)
    return image

def fn_bg(width: int =1400,
          height: int = 2993,
          hex: str = "#FFFFFF"
          ):
    color = hex_to_rgb(hex)
    return create_solid_color_bg(width=width,height=height,color=color)

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
