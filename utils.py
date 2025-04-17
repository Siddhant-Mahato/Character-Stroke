from PIL import Image, ImageDraw
import numpy as np

def strokes_to_image(strokes, size=(28, 28)):
    """Convert stroke points into a grayscale image"""
    img = Image.new("L", size, 255)  # White background
    draw = ImageDraw.Draw(img)
    for i in range(1, len(strokes)):
        if strokes[i][2] == 1:
            draw.line(
                [(strokes[i-1][0], strokes[i-1][1]), (strokes[i][0], strokes[i][1])],
                fill=0, width=3
            )
    return img

def prepare_image_for_model(img):
    img = img.resize((28, 28))         # Resize if needed
    arr = np.array(img)
    arr = arr.flatten() / 255.0        # Normalize
    return arr.reshape(1, -1)          # Shape for sklearn
