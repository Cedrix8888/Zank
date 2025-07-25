# 专业生成设计图的AI Agent
我们使用python版本为3.12的anaconda虚拟环境进行开发和测试
我们使用hugging_face社区的diffusers库进行基础的文生图
为了微调基础stable_diffusion模型以生成特定风格的图片(此处为特定的设计风格)，我们使用尝试以下方法
    1.使用prompt_technique将提示词优化成能生成特定风格图片的提示词
    2.微调扩散模型本身
为了生成带透明通道的图像，我们参考了lllyasviel的[layerdiffuse仓库](https://github.com/lllyasviel/LayerDiffuse_DiffusersCLI)