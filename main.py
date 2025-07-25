import torch
from diffusers.pipelines.pipeline_utils import DiffusionPipeline
from dotenv import load_dotenv
import os

load_dotenv()
hf_token=os.getenv("HF_ACCESS_TOKEN")
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, token=hf_token, use_safetensors=true, variant="fp16")
#cuda for NAVIDIA, mps for M series
pipe = pipe.to("mps")

prompt="A marketing poster promoting Coca-Cola"
image=pipe(prompt).images[0]
image.save("poster.png")
