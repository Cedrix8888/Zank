from algorithms.Rgb.rgb import gen_rgb
from utils.image import gen_img_path
from datetime import datetime
import uuid

async def layer_rgb(user_id: str = "zx",
                    width: int = 1400,
                    height: int = 2993,
                    color: str = "#000000",
                    is_output: bool = True,
                    file_format: str = "png",
                    ):
    
    img = gen_rgb(width, height, color)
    local_path = gen_img_path(user_id, is_output=is_output, file_format=file_format)
    img.save(local_path, format=file_format)

    return {
        "request_id": str(uuid.uuid4()),
        "local_path": local_path,
        "timestamp": datetime.now()
    }
    
    