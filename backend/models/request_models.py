from pydantic import BaseModel, Field

class BackgroundRequest(BaseModel):
    color: str = Field(..., description="Background color in hex format")
    width: int = Field(..., gt=0, description="Image width in pixels")
    height: int = Field(..., gt=0, description="Image height in pixels")

class LayerRequest(BaseModel):
    positive_prompt: str = Field(..., min_length=1, description="User input prompt")
    model_name: str = Field("gpt-3.5-turbo", description="AI model name")
    temperature: float = Field(0.7, ge=0, le=1, description="Generation randomness")