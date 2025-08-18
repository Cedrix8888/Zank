from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.request_models import LayerRequest  # 导入请求模型
from models.response_models import AIResultResponse, ErrorResponse  # 错误响应模型
from services.ai_service import gen_solid_layer  # 导入AI业务逻辑
from utils.logger import logger  # 导入日志工具
from security.api_key import get_api_key  # 导入API密钥验证依赖（如果需要）

router = APIRouter(
    prefix="/ai",
    responses={  # 全局响应模型
        400: {"model": ErrorResponse, "description": "无效请求"},
        500: {"model": ErrorResponse, "description": "服务器错误"}
    }
)

@router.post(
    "/generate",
    response_model=AIResultResponse,  # 明确响应数据结构
    summary="生成AI响应",
    description="接收用户提示词,调用AI模型生成响应内容"
)
async def solid_layer(
    request: LayerRequest,  # 请求数据（自动验证）
    api_key: str = Depends(get_api_key)  # 可选：API密钥验证
):
    try:
                
        # 调用服务层处理（业务逻辑与路由分离）
        result = await gen_solid_layer(
            prompt=request.prompt,
            model_name=request.model_name,  # 从请求中获取模型名称
            temperature=request.temperature  # 从请求中获取温度参数
        )
        
        # 返回符合响应模型的数据
        return GenerateResponse(
            request_id=result["request_id"],
            content=result["content"],
            model_used=request.model_name,
            timestamp=result["timestamp"]
        )
    
    except ValueError as e:
        # 处理业务逻辑错误（如无效参数）
        logger.warning(f"请求处理失败: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        # 处理未知错误
        logger.error(f"服务器处理错误: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI服务暂时不可用，请稍后再试"
        )
