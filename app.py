import gradio as gr
from bg_layer.bg import fn_bg
from clear import fn_bg_clear

with gr.Blocks(title="Zank Designer", css_paths="./bg_layer/bg.css") as demo:
    with gr.Row(elem_id="bg_page"):
        with gr.Column(scale=1, elem_id="bg_size"):
            width_bg = gr.Number(label="宽度(pixel)", value=1400)
            height_bg = gr.Number(label="高度(pixel)", value=2993)
        with gr.Column(scale=2, elem_id="bg_color"):
            color_bg = gr.ColorPicker(label="背景颜色", value="#FFFFFF")
        with gr.Column(scale=2, elem_id="img_size"):
            layer_bg = gr.Image(label="输出", format="png")
        with gr.Column(scale=1):
            button_bg_clear = gr.Button("清除")
            button_bg = gr.Button("提交")
        
    button_bg.click(fn=fn_bg, inputs=[width_bg,height_bg,color_bg], outputs=layer_bg)
    button_bg_clear.click(fn=fn_bg_clear, inputs=[], outputs=[layer_bg, color_bg])
     
demo.launch()