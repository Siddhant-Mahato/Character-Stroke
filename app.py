import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import json
import os
import time
import threading
import joblib

# ========== CONFIG ==========

NORMALIZATION_BASE = 400
MAX_POINTS = 100  # max (x,y,pen) triplets
CANVAS_SIZE = 400
DRAW_DELAY = 5  # milliseconds per point when replaying

# ========== FUNCTIONS ==========

def preprocess_stroke_data(points):
    norm_points = []
    for x, y, p in points:
        norm_points.extend([x / NORMALIZATION_BASE, y / NORMALIZATION_BASE, p])

    # Pad or truncate to MAX_POINTS * 3
    if len(norm_points) < MAX_POINTS * 3:
        norm_points += [0] * (MAX_POINTS * 3 - len(norm_points))
    else:
        norm_points = norm_points[: MAX_POINTS * 3]

    return np.array(norm_points).reshape(1, -1)


def extract_points_from_canvas(json_data):
    points = []
    if json_data is not None and "objects" in json_data:
        for obj in json_data["objects"]:
            if obj["type"] == "path":
                for cmd in obj["path"]:
                    if len(cmd) >= 3:
                        x, y = cmd[1], cmd[2]
                        pen = 0 if len(points) == 0 else 1
                        points.append((x, y, pen))
    return points


# ========== UI ==========

st.title("🖋 Hindi Character Stroke Prediction")

# Initialize or load the dataset
dataset = []
if os.path.exists("saved_strokes.json"):
    with open("saved_strokes.json", "r") as f:
        try:
            dataset = json.load(f)
        except json.JSONDecodeError:
            dataset = []

# Display current dataset size
st.write(f"Total Saved Strokes: {len(dataset)}")

canvas_result = st_canvas(
    fill_color="rgba(0, 0, 0, 1)",
    stroke_width=4,
    stroke_color="#000000",
    background_color="#FFFFFF",
    width=CANVAS_SIZE,
    height=CANVAS_SIZE,
    drawing_mode="freedraw",
    key="canvas",
)

# Extract and preprocess the stroke data
if canvas_result.json_data is not None:
    points = extract_points_from_canvas(canvas_result.json_data)
    st.write("Captured Points:", points)

    if len(points) > 0:
        data = preprocess_stroke_data(points)

        # Predict if model exists
        if os.path.exists("model.pkl"):
            model = joblib.load("model.pkl")
            pred = model.predict(data)[0]
            st.success(f"✅ Predicted Label: **{pred}**")
        else:
            st.warning("Model file `model.pkl` not found!")

# Save the drawing data
if st.button("Save Drawing"):
    if len(points) > 0:
        # Resample to ensure exactly MAX_POINTS
        total_points = len(points)
        max_allowed = MAX_POINTS

        # Resample if the number of points is more than max allowed
        if total_points > max_allowed:
            indices = np.linspace(0, total_points - 1, max_allowed, dtype=int)
            reduced_points = [points[i] for i in indices]
            reduced_points[0] = (
                reduced_points[0][0],
                reduced_points[0][1],
                0,
            )  # Optional stroke end marker
        else:
            reduced_points = points.copy()

        # Save the points
        dataset.append([[int(x), int(y), int(p)] for (x, y, p) in reduced_points])

        # Write to JSON file
        try:
            with open("saved_strokes.json", "w") as f:
                json.dump(dataset, f)
            st.success(f"Drawing saved! Total saved strokes: {len(dataset)}")
        except Exception as e:
            st.error(f"Error saving drawing: {str(e)}")

# Load the last saved drawing and display it
if st.button("Load Last Drawing"):
    if dataset:
        last_sample = dataset[-1]
        st.write(f"Loading Last Drawing with {len(last_sample)} Points")

        # Create a helper function to draw the last sample
        def draw_last_sample():
            canvas_result.json_data = {
                "objects": [
                    {
                        "type": "path",
                        "path": [(0, 0, 0, 0)]
                        + [(x, y, 0, 0) for x, y, _ in last_sample],
                    }
                ]
            }
            # Replay the drawing
            for x, y, _ in last_sample:
                time.sleep(DRAW_DELAY / 1000.0)

        threading.Thread(target=draw_last_sample).start()
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import json
import os
import time
import threading
import joblib

# ========== CONFIG ==========

NORMALIZATION_BASE = 400
MAX_POINTS = 100  # max (x,y,pen) triplets
CANVAS_SIZE = 400
DRAW_DELAY = 5  # milliseconds per point when replaying

# ========== FUNCTIONS ==========

def preprocess_stroke_data(points):
    norm_points = []
    for x, y, p in points:
        norm_points.extend([x / NORMALIZATION_BASE, y / NORMALIZATION_BASE, p])

    # Pad or truncate to MAX_POINTS * 3
    if len(norm_points) < MAX_POINTS * 3:
        norm_points += [0] * (MAX_POINTS * 3 - len(norm_points))
    else:
        norm_points = norm_points[: MAX_POINTS * 3]

    return np.array(norm_points).reshape(1, -1)


def extract_points_from_canvas(json_data):
    points = []
    if json_data is not None and "objects" in json_data:
        for obj in json_data["objects"]:
            if obj["type"] == "path":
                for cmd in obj["path"]:
                    if len(cmd) >= 3:
                        x, y = cmd[1], cmd[2]
                        pen = 0 if len(points) == 0 else 1
                        points.append((x, y, pen))
    return points


# ========== UI ==========

st.title("🖋 Hindi Character Stroke Prediction")

# Initialize or load the dataset
dataset = []
if os.path.exists("saved_strokes.json"):
    with open("saved_strokes.json", "r") as f:
        try:
            dataset = json.load(f)
        except json.JSONDecodeError:
            dataset = []

# Display current dataset size
st.write(f"Total Saved Strokes: {len(dataset)}")

canvas_result = st_canvas(
    fill_color="rgba(0, 0, 0, 1)",
    stroke_width=4,
    stroke_color="#000000",
    background_color="#FFFFFF",
    width=CANVAS_SIZE,
    height=CANVAS_SIZE,
    drawing_mode="freedraw",
    key="canvas",
)

# Extract and preprocess the stroke data
if canvas_result.json_data is not None:
    points = extract_points_from_canvas(canvas_result.json_data)
    st.write("Captured Points:", points)

    if len(points) > 0:
        data = preprocess_stroke_data(points)

        # Predict if model exists
        if os.path.exists("model.pkl"):
            model = joblib.load("model.pkl")
            pred = model.predict(data)[0]
            st.success(f"✅ Predicted Label: **{pred}**")
        else:
            st.warning("Model file `model.pkl` not found!")

# Save the drawing data
if st.button("Save Drawing"):
    if len(points) > 0:
        # Resample to ensure exactly MAX_POINTS
        total_points = len(points)
        max_allowed = MAX_POINTS

        # Resample if the number of points is more than max allowed
        if total_points > max_allowed:
            indices = np.linspace(0, total_points - 1, max_allowed, dtype=int)
            reduced_points = [points[i] for i in indices]
            reduced_points[0] = (
                reduced_points[0][0],
                reduced_points[0][1],
                0,
            )  # Optional stroke end marker
        else:
            reduced_points = points.copy()

        # Save the points
        dataset.append([[int(x), int(y), int(p)] for (x, y, p) in reduced_points])

        # Write to JSON file
        try:
            with open("saved_strokes.json", "w") as f:
                json.dump(dataset, f)
            st.success(f"Drawing saved! Total saved strokes: {len(dataset)}")
        except Exception as e:
            st.error(f"Error saving drawing: {str(e)}")

# Load the last saved drawing and display it
if st.button("Load Last Drawing"):
    if dataset:
        last_sample = dataset[-1]
        st.write(f"Loading Last Drawing with {len(last_sample)} Points")

        # Create a helper function to draw the last sample
        def draw_last_sample():
            canvas_result.json_data = {
                "objects": [
                    {
                        "type": "path",
                        "path": [(0, 0, 0, 0)]
                        + [(x, y, 0, 0) for x, y, _ in last_sample],
                    }
                ]
            }
            # Replay the drawing
            for x, y, _ in last_sample:
                time.sleep(DRAW_DELAY / 1000.0)

        threading.Thread(target=draw_last_sample).start()
