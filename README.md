# Sketch Image Generator

## Overview

This repository contains a simple image sketch generator using Gradio and OpenCV. The script takes an input image and transforms it into a sketch-like version using various image processing techniques.

## Features

- Converts input image to a sketch
- Utilizes Gradio for easy user interaction
- Integrates OpenCV for image processing

## Requirements

- Python 3.x
- Gradio
- OpenCV
- Numpy

## Installation

You can install the required packages using the following command:

```bash
pip install gradio opencv-python numpy
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/greatwhite9/sketch-image-generator.git
```

2. Navigate to the project directory:

```bash
cd sketch-image-generator
```

3. Run the script:

```bash
python sketch_generator.py
```

4. Access the Gradio interface in your web browser at the provided URL.

## How it Works

The `sketch` function in the script takes an image as input, converts it to a grayscale image, inverts the colors, applies a Gaussian blur, and finally, generates the sketch-like effect. The Gradio interface allows users to upload an image and view the transformed output.

## Customization

Feel free to customize the script or integrate it into your projects. You can modify the parameters of the image processing functions or extend the functionality as needed.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or create a pull request.

## Acknowledgments

- Gradio: [https://www.gradio.app/](https://www.gradio.app/)
- OpenCV: [https://opencv.org/](https://opencv.org/)
- Numpy: [https://numpy.org/](https://numpy.org/)

Thank you for using the Sketch Image Generator! If you have any questions or concerns, please feel free to reach out.
