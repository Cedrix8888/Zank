import os
import uuid
from datetime import datetime
from config import AI_IMAGE_ROOT

def generate_image_path(user_id, is_output=true, file_format="png"):
    # 按用户ID和日期分目录
    date_str = datetime.now().strftime("%Y%m%d")
    user_dir = AI_IMAGE_ROOT / f"user_{user_id}" / date_str
    os.makedirs(user_dir, exist_ok=True)
    prefix = "output_" if is_output else "input_"
    # 生成唯一文件名（UUID+原格式）
    file_name = f"{prefix}img_{uuid.uuid4().hex}.{file_format}"
    
    # 返回完整本地路径和数据库存储路径
    local_path = user_dir / file_name
    # 数据库存储相对路径（相对于静态资源根目录，便于Web访问）
    db_path = f"{prefix}images/user_{user_id}/{date_str}/{file_name}"
    return local_path, db_path