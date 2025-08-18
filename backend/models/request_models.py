from pydantic import BaseModel, Field

class LayerRequest(BaseModel):
    color: str = Field(description="Background color in hex format")
    width: int = Field(..., gt=0, description="Image width in pixels")
    height: int = Field(..., gt=0, description="Image height in pixels")
    positive_prompt: str = Field(..., min_length=1, description="User input prompt")
    negative_prompt: str = Field(..., min_length=1, description="User input prompt")
