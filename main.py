import torch
from diffusers import StableDiffusion3Pipeline
from dotenv import load_dotenv
import os

load_dotenv()
hf_token=os.getenv("HF_ACCESS_TOKEN")
pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3.5-large", torch_dtype=torch.bfloat16, token=hf_token)
#cuda for NAVIDIA, mps for M series
pipe = pipe.to("cuda")

prompt="A marketing poster promoting Coca-Cola"
image=pipe(
    prompt,
    num_inference_steps=28,
    guidance_scale=3.5,
).images[0]
image.save("poster.png")
