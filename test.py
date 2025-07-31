import safetensors.torch as sf

# 加载权重
weights = sf.load_file("./models/ld_diffusers_sdxl_vae_transparent_decoder.safetensors")

# 遍历键名，找 time_emb_proj
time_emb_keys = [k for k in weights.keys() if "time_emb_proj" in k]

if time_emb_keys:
    # 取第一个 time_emb_proj 的 shape（通常是 [temb_channels, ...]）
    # 例如：若 shape 是 [1280, 320]，则 temb_channels=1280
    temb_channels = weights[time_emb_keys[0]].shape[0]
    print(f"temb_channels = {temb_channels}")
else:
    print("未找到 time_emb_proj 相关键，模型可能没用到时间嵌入")
