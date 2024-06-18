import gradio as gr
from deoldify.visualize import *

colorizer = get_image_colorizer(artistic=True)

def colorize_image(image):
    result = colorizer.get_transformed_image(image)
    return result

gr.Interface(
    fn=colorize_image,
    inputs=gr.inputs.Image(type="file", label="Upload Image"),
    outputs=gr.outputs.Image(type="file", label="Colorized Image"),
    title="DeOldify",
    description="Colorize black and white images using DeOldify."
).launch()
