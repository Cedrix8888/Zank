from algorithms.Img_gen.Rgb.rgb import gen_rgb
from algorithms.Img_gen.Trans.trans import gen_trans
from utils.image import gen_img_path
from datetime import datetime
import uuid

async def layer_rgb(user_id: str = "zx",
                    width: int = 1400,
                    height: int = 2993,
                    is_output: bool = True,
                    file_format: str = "png",
                    color: str = "#000000",
                    ):
    
    img = gen_rgb(width, height, color)
    local_path = gen_img_path(user_id, is_output=is_output, file_format=file_format)
    img.save(local_path, format=file_format)

    return {
        "request_id": str(uuid.uuid4()),
        "local_path": local_path,
        "timestamp": datetime.now()
    }

async def layer_trans(user_id: str = "zx",
                      width: int = 1400,
                      height: int = 2993,
                      is_output: bool = True,
                      file_format: str = "png",
                      prompt_pos: str = "glass bottle, high quality",
                      prompt_neg: str = "face asymmetry, eyes asymmetry, deformed eyes, open mouth"
                      ):
    
    img = gen_trans(width, height, prompt_pos, prompt_neg)[0]
    local_path = gen_img_path(user_id, is_output=is_output, file_format=file_format)
    img.save(local_path, format=file_format)

    return {
        "request_id": str(uuid.uuid4()),
        "local_path": local_path,
        "timestamp": datetime.now()
    }
    