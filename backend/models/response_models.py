from pydantic import BaseModel, Field
from datetime import datetime

class BaseResponse(BaseModel):
    user_id: str = Field(default="zx", description="用户ID")
    request_id: str = Field(..., description="请求唯一标识ID")
    local_path: str = Field(..., description="生成图像的本地存储路径")
    timestamp: datetime = Field(default_factory=datetime.now, description="请求处理时间(UTC)")
    success: bool = Field(default=True, description="请求是否成功")
    message: str = Field(default="操作成功", description="状态消息")

class RgbResponse(BaseResponse):
    color: tuple = Field(default=(255, 255, 255), description="生成图像的颜色")
    
class LayerResponse(BaseResponse):
    prompt_pos: str = Field("glass bottle, high quality", description="用户输入的正面提示词")
    prompt_neg: str = Field("face asymmetry, eyes asymmetry, deformed eyes, open mouth", description="用户输入的负面提示词")
    class Config:
        from_attributes = True
        
class SvgResponse(BaseResponse):
    text: str = Field(..., description="生成的SVG文本内容")

class ErrorResponse(BaseModel):
    user_id: str = Field("zx", description="用户ID")
    success: bool = Field(False, description="请求失败")
    error_message: str = Field(..., description="错误详细信息")
    timestamp: datetime = Field(default_factory=datetime.now, description="错误发生时间")
    