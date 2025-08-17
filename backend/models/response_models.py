from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Dict

class BaseResponse(BaseModel):
    """基础响应模型,所有响应模型的父类"""
    success: bool = Field(True, description="请求是否成功")
    message: str = Field("操作成功", description="状态消息")
    request_id: str = Field(..., description="请求唯一标识ID")

class AIResultResponse(BaseResponse):
    """AI生成结果响应模型"""
    content: str = Field(..., description="AI生成的内容")
    model_used: str = Field(..., description="使用的AI模型名称")
    processing_time: Optional[str] = Field(None, description="处理时间(毫秒)")
    created_at: datetime = Field(..., description="生成时间(UTC)")
    
    class Config:
        """配置类,允许从ORM模型实例创建响应模型"""
        orm_mode = True

class AIHistoryItem(BaseModel):
    """历史记录项模型,用于展示用户的AI交互历史"""
    id: str = Field(..., description="记录ID")
    prompt: str = Field(..., description="用户输入的提示词")
    content_preview: str = Field(..., description="AI生成内容的预览(前50字符)")
    model_name: str = Field(..., description="使用的AI模型")
    created_at: datetime = Field(..., description="生成时间")

class AIHistoryResponse(BaseResponse):
    """AI历史记录列表响应模型"""
    total_count: int = Field(..., description="总记录数")
    items: List[AIHistoryItem] = Field(..., description="历史记录列表")
    page: int = Field(..., description="当前页码")
    page_size: int = Field(..., description="每页记录数")
    total_pages: int = Field(..., description="总页数")

class ModelInfo(BaseModel):
    """AI模型信息模型,用于展示可用模型"""
    name: str = Field(..., description="模型名称")
    description: str = Field(..., description="模型描述")
    capabilities: List[str] = Field(..., description="模型能力列表")
    is_available: bool = Field(..., description="模型是否可用")
    performance: Dict[str, str] = Field(..., description="模型性能指标")

class ModelListResponse(BaseResponse):
    """模型列表响应模型"""
    models: List[ModelInfo] = Field(..., description="可用AI模型列表")
    total_models: int = Field(..., description="模型总数")

class ErrorResponse(BaseModel):
    """错误响应模型,用于统一错误返回格式"""
    success: bool = Field(False, description="请求失败")
    error_code: str = Field(..., description="错误代码")
    error_message: str = Field(..., description="错误详细信息")
    request_id: str = Field(..., description="请求唯一标识ID")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="错误发生时间")
    