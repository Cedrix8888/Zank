from fastapi import APIRouter, Depends, HTTPException, status
from models.request_models import RgbRequest, LayerRequest
from models.response_models import RgbResponse, LayerResponse, ErrorResponse
from services.ai.ai_service import layer_rgb, layer_trans
from utils.security import get_api_key
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
    dependencies=[Depends(get_api_key)],
    responses={
        400: {"model": ErrorResponse, "description": "无效请求"},
        401: {"model": ErrorResponse, "description": "API Key 验证失败"},  
        500: {"model": ErrorResponse, "description": "服务器错误"}
    }
)

@router.post(
    path="/rgb",
    response_model=RgbResponse,  
    summary="生成RGB图像",
    description="生成指定颜色的RGB图像",
)
async def request_rgb(request: RgbRequest):
    try:
        result = await layer_rgb(
            user_id=request.user_id,
            width=request.width,
            height=request.height,
            color=request.color
        )
        
        return RgbResponse(
            request_id=result["request_id"],
            local_path=result["local_path"],
            timestamp=result["timestamp"]
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "user_id": request.user_id,
                "error_message": str(e),
                }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "user_id": request.user_id,
                "error_message": "服务器内部错误，请稍后再试。",
            }
        )
        
@router.post(
    path="/layer",
    response_model=LayerResponse,  
    summary="生成单图层图像",
    description="根据传入文本生成带透明通道的单图层图像",
)
async def request_layer(request: LayerRequest):
    try:
        result = await layer_trans(
            user_id=request.user_id,
            width=request.width,
            height=request.height,
            prompt_pos=request.prompt_pos,
            prompt_neg=request.prompt_neg
        )
        
        return LayerResponse(
            request_id=result["request_id"],
            local_path=result["local_path"],
            timestamp=result["timestamp"],
            prompt_pos=request.prompt_pos,
            prompt_neg=request.prompt_neg
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "user_id": request.user_id,
                "error_message": str(e),
                }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "user_id": request.user_id,
                "error_message": "服务器内部错误，请稍后再试。",
            }
        )
