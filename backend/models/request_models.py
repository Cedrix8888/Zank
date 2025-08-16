from pydantic import BaseModel, Field
class PromptRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="用户输入的提示词")
    model_name: str = Field("gpt-3.5-turbo", description="要使用的AI模型名称")
    temperature: float = Field(0.7, ge=0, le=1, description="生成随机性，0-1之间")