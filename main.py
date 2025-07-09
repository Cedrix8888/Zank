from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", use_safetensors=True)
# mps for M series; cuda for NVIDIA series
pipeline.to("mps")
prompt = "A marketing poster promoting Coca-Cola"
image = pipeline(prompt).images[0]
image.save("poster.png")