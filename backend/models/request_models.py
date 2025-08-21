from pydantic import BaseModel, Field

class RgbRequest(BaseModel):
    user_id: str = Field("zx", description="User ID for image generation")
    color: str = Field("#000000", description="Background color in hex format")
    width: int = Field(1400, gt=0, description="Image width in pixels")
    height: int = Field(2993, gt=0, description="Image height in pixels")

class LayerRequest(BaseModel):
    user_id: str = Field("zx", description="User ID for image generation")
    width: int = Field(1400, gt=0, description="Image width in pixels")
    height: int = Field(2993, gt=0, description="Image height in pixels")
    positive_prompt: str = Field(..., min_length=1, description="User input prompt")
    negative_prompt: str = Field(..., min_length=1, description="User input prompt")
