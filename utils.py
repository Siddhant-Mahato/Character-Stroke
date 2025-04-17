import numpy as np
import cv2

def preprocess_strokes(strokes, canvas_size=(256, 256)):
    if not strokes:
        return None

    all_points = [(x, y) for stroke in strokes for x, y in stroke]
    if not all_points:
        return None

    xs, ys = zip(*all_points)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    norm_strokes = []
    for stroke in strokes:
        norm_stroke = [
            (
                int((x - min_x) / (max_x - min_x + 1e-5) * (canvas_size[0] - 1)),
                int((y - min_y) / (max_y - min_y + 1e-5) * (canvas_size[1] - 1))
            ) for x, y in stroke
        ]
        norm_strokes.append(norm_stroke)

    return norm_strokes

def stroke_to_image(strokes, canvas_size=(256, 256)):
    image = np.ones(canvas_size, dtype=np.uint8) * 255
    for stroke in strokes:
        for i in range(1, len(stroke)):
            cv2.line(image, stroke[i-1], stroke[i], color=0, thickness=3)
    return image


# File: train_model.py
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# For demonstration, using sklearn's digits dataset
digits = load_digits()
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='rbf', probability=True)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, preds)}")

joblib.dump({'model': model}, 'hindi_digit_model.pkl')
print("✅ Model saved successfully!")
