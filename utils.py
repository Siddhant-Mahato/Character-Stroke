import numpy as np
from PIL import Image
import joblib
from sklearn.preprocessing import StandardScaler

# Function to process stroke data
def process_stroke_data(stroke_data, max_points=100):
    total = len(stroke_data)
    
    # Downsample or pad to max_points
    if total > max_points:
        indices = np.linspace(0, total - 1, max_points, dtype=int)
        stroke_data = [stroke_data[i] for i in indices]
    elif total < max_points:
        stroke_data += [[0, 0, 0]] * (max_points - total)
    
    return stroke_data

# Function to convert stroke data into image
def strokes_to_image(stroke_data, canvas_size=400):
    # Initialize a blank canvas (white background)
    image = Image.new('L', (canvas_size, canvas_size), color=255)
    draw = ImageDraw.Draw(image)
    
    # Draw the strokes on the canvas
    for stroke in stroke_data:
        x, y, p = stroke
        if p == 1:  # Pen down
            draw.line([prev_x, prev_y, x, y], fill=0, width=4)
        prev_x, prev_y = x, y
    
    return image

# Function to load the trained model
def load_model(model_path="hindi_digit_model.pkl"):
    return joblib.load(model_path)

# Function to predict the character using the trained model
def predict_character(stroke_data, model, scaler=None):
    # Preprocess stroke data
    processed_data = process_stroke_data(stroke_data)
    
    # Convert to feature vector
    feature_vector = np.array(processed_data).flatten().reshape(1, -1)
    
    # Standardize the feature vector (if needed)
    if scaler:
        feature_vector = scaler.transform(feature_vector)
    
    # Predict the digit
    prediction = model.predict(feature_vector)
    return prediction[0]

# Function to save the model
def save_model(model, model_path="hindi_digit_model.pkl"):
    joblib.dump(model, model_path)
