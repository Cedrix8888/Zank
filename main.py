from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", use_safetensors=True)
pipeline.to(torch.device("mps"))
image = pipeline("An image of a squirrel in Picasso style").images[0]
image.save("squirrel.png")