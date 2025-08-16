from datetime import datetime
import uuid

async def process_ai_request(prompt: str, model_name: str, temperature: float):
    # 1. 验证模型是否支持
    supported_models = ["gpt-3.5-turbo", "gpt-4", "local-llama"]
    if model_name not in supported_models:
        raise ValueError(f"不支持的模型: {model_name}，支持的模型有: {supported_models}")
    
    # 2. 调用对应AI模型（示例逻辑）
    if model_name.startswith("gpt"):
        content = await call_openai_api(prompt, model_name, temperature)
    else:
        content = await call_local_model(prompt, model_name, temperature)
    
    # 3. 返回处理结果
    return {
        "request_id": str(uuid.uuid4()),  # 生成唯一请求ID
        "content": content,
        "timestamp": datetime.utcnow()
    }