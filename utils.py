# utils.py

import numpy as np
from PIL import Image, ImageDraw
import cv2

def preprocess_strokes(strokes, image_size=(28, 28)):
    """
    Convert raw stroke data into a fixed-length vector suitable for the model.
    """
    stroke_img = stroke_to_image(strokes, image_size=image_size)
    gray = cv2.cvtColor(np.array(stroke_img), cv2.COLOR_RGB2GRAY)
    resized = cv2.resize(gray, image_size, interpolation=cv2.INTER_AREA)
    flat = resized.flatten() / 255.0  # Normalize
    return flat

def stroke_to_image(strokes, image_size=(280, 280)):
    """
    Convert stroke data into an image using PIL.
    """
    img = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(img)

    for stroke in strokes:
        if len(stroke) < 2:
            continue
        for i in range(len(stroke) - 1):
            if stroke[i][2] == 1 and stroke[i+1][2] == 1:
                draw.line([stroke[i][:2], stroke[i+1][:2]], fill="black", width=5)

    return img
