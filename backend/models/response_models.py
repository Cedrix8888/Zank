from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class BaseResponse(BaseModel):
    """基础响应模型,所有响应模型的父类"""
    success: bool = Field(True, description="请求是否成功")
    message: str = Field("操作成功", description="状态消息")
    request_id: str = Field(..., description="请求唯一标识ID")

class AIResultResponse(BaseResponse):
    """AI生成结果响应模型"""
    positive_prompt: Optional(str) = Field(None, description="用户输入的正面提示词")
    negative_prompt: Optional[str] = Field(None, description="用户输入的负面提示词")
    width: Optional(int) = Field(None, gt=0, description="生成图像的宽度")
    height: Optional(int) = Field(None, gt=0, description="生成图像的高度")
    content: str = Field(..., description="AI生成图像的路径")
    created_at: datetime = Field(..., description="生成时间(UTC)")
    
    class Config:
        """配置类,允许从ORM模型实例创建响应模型"""
        orm_mode = True

class AIHistoryItem(BaseModel):
    """历史记录项模型,用于展示用户的AI交互历史"""
    id: str = Field(..., description="记录ID")
    prompt: str = Field(..., description="用户输入的提示词")
    created_at: datetime = Field(..., description="生成时间")

class ErrorResponse(BaseModel):
    """错误响应模型,用于统一错误返回格式"""
    success: bool = Field(False, description="请求失败")
    error_code: str = Field(..., description="错误代码")
    error_message: str = Field(..., description="错误详细信息")
    request_id: str = Field(..., description="请求唯一标识ID")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="错误发生时间")
    