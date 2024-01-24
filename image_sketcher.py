import gradio as gr
import cv2
import numpy as np

def sketch(image):
    # Convert the Gradio Image object to a numpy array
    image = np.array(image)
    grey_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert_img=cv2.bitwise_not(grey_img)
    blur_img=cv2.GaussianBlur(invert_img, (21,21),0)
    invblur_img=cv2.bitwise_not(blur_img)
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    return sketch_img

interface = gr.Interface(fn=sketch,
                         inputs=gr.Image(),
                         outputs="image")
interface.launch()
