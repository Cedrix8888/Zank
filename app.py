import gradio as gr

with gr.Blocks() as demo:
    name = gr.Textbox(label="name")
    intensity = gr.Slider(minimum=1, maximum=10, value=2, label="intensity")
    greet = gr.Textbox(label="greeting")
    clear_btn = gr.Button("Clear")
    submit_btn = gr.Button("Submit")
    flag_btn = gr.Button("Flag")
    
    def submit_fn(name_val, intensity_val):
        return f"Hello {name_val}, intensity is {intensity_val}"
    submit_btn.click(fn=submit_fn, inputs=[name, intensity], outputs=greet)

    demo.launch()