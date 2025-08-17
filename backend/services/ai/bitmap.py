from diffusers.pipelines.pipeline_utils import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")
prompt = input("Enter your prompt: ")

images = pipe(prompt=prompt,
              height=2993,
              width=1400
              ).images[0]

images.save("./imgs/outputs/bg.png")
