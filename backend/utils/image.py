import os
import uuid
from datetime import datetime
from config import AI_IMAGE_ROOT

def gen_img_path(user_id, is_output=True, file_format="png"):
    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    user_dir = AI_IMAGE_ROOT / f"user_{user_id}" / date_str / "output" if is_output else "input"
    os.makedirs(user_dir, exist_ok=True)
    prefix = "output_" if is_output else "input_"
    file_name = f"{prefix}img_{uuid.uuid4().hex}.{file_format}"
    local_path = user_dir / file_name
    return local_path

def hex_rgb(hex: str = "#000000"):
    hex = hex.lstrip("#")
    if len(hex) == 3:
        hex = ''.join([c * 2 for c in hex])
    if len(hex) != 6:
        raise ValueError("无效的十六进制颜色格式, 应为#RRGGBB形式")
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))