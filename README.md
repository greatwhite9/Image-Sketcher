# Image Sketch Generator

## Overview

This project is an **Image Sketch Generator** that transforms images into sketch-like drawings using **OpenCV** and **NumPy**. The interface is built using **Gradio**, allowing users to easily upload and convert images into sketches through a web interface.

## Features

- Converts any input image into a pencil sketch
- Built using **Gradio** for a simple and user-friendly interface
- Employs **OpenCV** for efficient image processing

## Requirements

- Python 3.x
- Gradio
- OpenCV
- NumPy

## Installation

Install the necessary packages with the following command:

```bash
pip install gradio opencv-python numpy
```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/greatwhite9/Image-Sketcher.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Image-Sketcher
    ```

3. Run the script:

    ```bash
    python image_sketcher.py
    ```

4. After running the script, access the **Gradio** interface via the link provided in the terminal. You can then upload an image and see its sketch-like transformation in real time.

## How it Works

The `sketch` function follows these steps to create the sketch effect:
1. Converts the input image to grayscale.
2. Inverts the grayscale image.
3. Applies a **Gaussian blur** to the inverted image.
4. Inverts the blurred image.
5. Divides the grayscale image by the inverted blurred image to generate the final sketch.

Gradio serves as the web-based interface, making it easy for users to interact with the tool by uploading images and viewing their sketched versions.

## Customization

You can adjust the image processing parameters, such as the **Gaussian blur** kernel size or the scaling factor in the `cv2.divide()` function, to fine-tune the sketching effect.

## Contributing

Contributions are welcome! If you have ideas for new features, optimizations, or bug fixes, feel free to create an issue or submit a pull request.
