from pydantic import BaseModel, Field

class RgbRequest(BaseModel):
    user_id: str = Field("zx", description="User ID for image generation")
    width: int = Field(1400, gt=0, description="Image width in pixels")
    height: int = Field(2993, gt=0, description="Image height in pixels")
    color: str = Field("#000000", description="Background color in hex format")

class LayerRequest(BaseModel):
    user_id: str = Field("zx", description="User ID for image generation")
    width: int = Field(1400, gt=0, description="Image width in pixels")
    height: int = Field(2993, gt=0, description="Image height in pixels")
    prompt_pos: str = Field("glass bottle, high quality", min_length=1, description="User input prompt")
    prompt_neg: str = Field("face asymmetry, eyes asymmetry, deformed eyes, open mouth", min_length=1, description="User input prompt")
