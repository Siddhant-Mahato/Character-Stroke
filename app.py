

# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# import numpy as np
# import json
# import os
# import time
# import threading
# import joblib

# # ========== CONFIG ==========

# NORMALIZATION_BASE = 400
# MAX_POINTS = 100  # max (x,y,pen) triplets
# CANVAS_SIZE = 400
# DRAW_DELAY = 5  # milliseconds per point when replaying



# # ========== FUNCTIONS ==========


# def preprocess_stroke_data(points):
#     norm_points = []
#     for x, y, p in points:
#         norm_points.extend([x / NORMALIZATION_BASE, y / NORMALIZATION_BASE, p])

#     # Pad or truncate to MAX_POINTS * 3
#     if len(norm_points) < MAX_POINTS * 3:
#         norm_points += [0] * (MAX_POINTS * 3 - len(norm_points))
#     else:
#         norm_points = norm_points[: MAX_POINTS * 3]

#     return np.array(norm_points).reshape(1, -1)


# def extract_points_from_canvas(json_data):
#     points = []
#     if json_data is not None and "objects" in json_data:
#         for obj in json_data["objects"]:
#             if obj["type"] == "path":
#                 for cmd in obj["path"]:
#                     if len(cmd) >= 3:
#                         x, y = cmd[1], cmd[2]
#                         pen = 0 if len(points) == 0 else 1
#                         points.append((x, y, pen))
#     return points


# # ========== UI ===========

# st.title("🖋 Hindi Character Stroke Prediction")

# # Initialize or load the dataset
# dataset = []
# if os.path.exists("saved_strokes.json"):
#     with open("saved_strokes.json", "r") as f:
#         try:
#             dataset = json.load(f)
#         except json.JSONDecodeError:
#             dataset = []

# # Display current dataset size
# st.write(f"Total Saved Strokes: {len(dataset)}")

# canvas_result = st_canvas(
#     fill_color="rgba(0, 0, 0, 1)",
#     stroke_width=4,
#     stroke_color="#000000",
#     background_color="#FFFFFF",
#     width=CANVAS_SIZE,
#     height=CANVAS_SIZE,
#     drawing_mode="freedraw",
#     key="canvas",
# )

# # Extract and preprocess the stroke data
# if canvas_result.json_data is not None:
#     points = extract_points_from_canvas(canvas_result.json_data)
#     st.write("Captured Points:", points)

#     if len(points) > 0:
#         data = preprocess_stroke_data(points)

#         # Predict if model exists
#         if os.path.exists("model.pkl"):
#             model = joblib.load("model.pkl")
#             pred = model.predict(data)[0]
#             st.success(f"✅ Predicted Label: **{pred}**")
#         else:
#             st.warning("Model file `model.pkl` not found!")

# # Save the drawing data
# if st.button("Save Drawing"):
#     if len(points) > 0:
#         # Resample to ensure exactly MAX_POINTS
#         total_points = len(points)
#         max_allowed = MAX_POINTS

#         # Resample if the number of points is more than max allowed
#         if total_points > max_allowed:
#             indices = np.linspace(0, total_points - 1, max_allowed, dtype=int)
#             reduced_points = [points[i] for i in indices]
#             reduced_points[0] = (
#                 reduced_points[0][0],
#                 reduced_points[0][1],
#                 0,
#             )  # Optional stroke end marker
#         else:
#             reduced_points = points.copy()

#         # Save the points
#         dataset.append([[int(x), int(y), int(p)] for (x, y, p) in reduced_points])

#         # Write to JSON file
#         try:
#             with open("saved_strokes.json", "w") as f:
#                 json.dump(dataset, f)
#             st.success(f"Drawing saved! Total saved strokes: {len(dataset)}")
#         except Exception as e:
#             st.error(f"Error saving drawing: {str(e)}")

# # Load the last saved drawing and display it
# if st.button("Load Last Drawing"):
#     if dataset:
#         last_sample = dataset[-1]
#         st.write(f"Loading Last Drawing with {len(last_sample)} Points")

#         # Create a helper function to draw the last sample
#         def draw_last_sample():
#             canvas_result.json_data = {
#                 "objects": [
#                     {
#                         "type": "path",
#                         "path": [(0, 0, 0, 0)]
#                         + [(x, y, 0, 0) for x, y, _ in last_sample],
#                     }
#                 ]
#             }
#             # Replay the drawing
#             for x, y, _ in last_sample:
#                 time.sleep(DRAW_DELAY / 1000.0)

#         threading.Thread(target=draw_last_sample).start()
# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# import numpy as np
# import json
# import os
# import time
# import threading
# import joblib

# # ========== CONFIG ==========

# NORMALIZATION_BASE = 400
# MAX_POINTS = 100  # max (x,y,pen) triplets
# CANVAS_SIZE = 400
# DRAW_DELAY = 5  # milliseconds per point when replaying

# # ========== FUNCTIONS ==========

# def preprocess_stroke_data(points):
#     norm_points = []
#     for x, y, p in points:
#         norm_points.extend([x / NORMALIZATION_BASE, y / NORMALIZATION_BASE, p])

#     # Pad or truncate to MAX_POINTS * 3
#     if len(norm_points) < MAX_POINTS * 3:
#         norm_points += [0] * (MAX_POINTS * 3 - len(norm_points))
#     else:
#         norm_points = norm_points[: MAX_POINTS * 3]

#     return np.array(norm_points).reshape(1, -1)


# def extract_points_from_canvas(json_data):
#     points = []
#     if json_data is not None and "objects" in json_data:
#         for obj in json_data["objects"]:
#             if obj["type"] == "path":
#                 for cmd in obj["path"]:
#                     if len(cmd) >= 3:
#                         x, y = cmd[1], cmd[2]
#                         pen = 0 if len(points) == 0 else 1
#                         points.append((x, y, pen))
#     return points


# # ========== UI ==========

# st.title("🖋 Hindi Character Stroke Prediction")

# # Initialize or load the dataset
# dataset = []
# if os.path.exists("saved_strokes.json"):
#     with open("saved_strokes.json", "r") as f:
#         try:
#             dataset = json.load(f)
#         except json.JSONDecodeError:
#             dataset = []

# # Display current dataset size
# st.write(f"Total Saved Strokes: {len(dataset)}")

# canvas_result = st_canvas(
#     fill_color="rgba(0, 0, 0, 1)",
#     stroke_width=4,
#     stroke_color="#000000",
#     background_color="#FFFFFF",
#     width=CANVAS_SIZE,
#     height=CANVAS_SIZE,
#     drawing_mode="freedraw",
#     key="canvas",
# )

# # Extract and preprocess the stroke data
# if canvas_result.json_data is not None:
#     points = extract_points_from_canvas(canvas_result.json_data)
#     st.write("Captured Points:", points)

#     if len(points) > 0:
#         data = preprocess_stroke_data(points)

#         # Predict if model exists
#         if os.path.exists("model.pkl"):
#             model = joblib.load("model.pkl")
#             pred = model.predict(data)[0]
#             st.success(f"✅ Predicted Label: **{pred}**")
#         else:
#             st.warning("Model file `model.pkl` not found!")

# # Save the drawing data
# if st.button("Save Drawing"):
#     if len(points) > 0:
#         # Resample to ensure exactly MAX_POINTS
#         total_points = len(points)
#         max_allowed = MAX_POINTS

#         # Resample if the number of points is more than max allowed
#         if total_points > max_allowed:
#             indices = np.linspace(0, total_points - 1, max_allowed, dtype=int)
#             reduced_points = [points[i] for i in indices]
#             reduced_points[0] = (
#                 reduced_points[0][0],
#                 reduced_points[0][1],
#                 0,
#             )  # Optional stroke end marker
#         else:
#             reduced_points = points.copy()

#         # Save the points
#         dataset.append([[int(x), int(y), int(p)] for (x, y, p) in reduced_points])

#         # Write to JSON file
#         try:
#             with open("saved_strokes.json", "w") as f:
#                 json.dump(dataset, f)
#             st.success(f"Drawing saved! Total saved strokes: {len(dataset)}")
#         except Exception as e:
#             st.error(f"Error saving drawing: {str(e)}")

# # Load the last saved drawing and display it
# if st.button("Load Last Drawing"):
#     if dataset:
#         last_sample = dataset[-1]
#         st.write(f"Loading Last Drawing with {len(last_sample)} Points")

#         # Create a helper function to draw the last sample
#         def draw_last_sample():
#             canvas_result.json_data = {
#                 "objects": [
#                     {
#                         "type": "path",
#                         "path": [(0, 0, 0, 0)]
#                         + [(x, y, 0, 0) for x, y, _ in last_sample],
#                     }
#                 ]
#             }
#             # Replay the drawing
#             for x, y, _ in last_sample:
#                 time.sleep(DRAW_DELAY / 1000.0)

#         threading.Thread(target=draw_last_sample).start()


# -------------------------------------------------------------------------------------------------------------------------------

# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# import numpy as np
# import json
# import os
# import joblib

# # ========== CONFIG ========== #
# NORMALIZATION_BASE = 400
# MAX_POINTS = 100
# MIN_POINTS = 80
# CANVAS_SIZE = 400

# # ========== FUNCTIONS ========== #

# def preprocess_stroke_data(points):
#     norm_points = []
#     for x, y, p in points:
#         norm_points.extend([x / NORMALIZATION_BASE, y / NORMALIZATION_BASE, p])
#     if len(norm_points) < MAX_POINTS * 3:
#         norm_points += [0] * (MAX_POINTS * 3 - len(norm_points))
#     else:
#         norm_points = norm_points[:MAX_POINTS * 3]
#     return np.array(norm_points).reshape(1, -1)

# def extract_points_from_canvas(json_data):
#     points = []
#     if json_data is not None and "objects" in json_data:
#         for obj in json_data["objects"]:
#             if obj["type"] == "path":
#                 for cmd in obj["path"]:
#                     if len(cmd) >= 3:
#                         x, y = cmd[1], cmd[2]
#                         pen = 0 if len(points) == 0 else 1
#                         points.append((x, y, pen))
#     return points

# # ========== UI ========== #

# st.title("🖋 Hindi Character Stroke Prediction")

# # Load dataset
# dataset = []
# if os.path.exists("saved_strokes.json"):
#     with open("saved_strokes.json", "r") as f:
#         try:
#             dataset = json.load(f)
#         except json.JSONDecodeError:
#             dataset = []

# st.write(f"📦 Total Saved Strokes: **{len(dataset)}**")

# # UI mode switch
# mode = st.radio("Select Mode:", ["✏️ Draw New", "🔁 Replay Last"])

# if mode == "✏️ Draw New":
#     canvas_result = st_canvas(
#         fill_color="rgba(0, 0, 0, 1)",
#         stroke_width=4,
#         stroke_color="#000000",
#         background_color="#FFFFFF",
#         width=CANVAS_SIZE,
#         height=CANVAS_SIZE,
#         drawing_mode="freedraw",
#         key="canvas_draw",
#     )

#     if canvas_result.json_data is not None:
#         points = extract_points_from_canvas(canvas_result.json_data)
#         st.write("🧠 Captured Points:", points)

#         if len(points) > 0:
#             data = preprocess_stroke_data(points)

#             if os.path.exists("model.pkl"):
#                 model = joblib.load("model.pkl")
#                 pred = model.predict(data)[0]
#                 st.success(f"✅ Predicted Label: **{pred}**")
#             else:
#                 st.warning("⚠️ Model file `model.pkl` not found!")

#     if st.button("💾 Save Drawing"):
#         if len(points) > 0:
#             total_points = len(points)

#             if total_points < MIN_POINTS:
#                 st.warning(f"⚠️ Draw more! Minimum {MIN_POINTS} points required to save.")
#             else:
#                 # Downsample if more than MAX_POINTS
#                 if total_points > MAX_POINTS:
#                     indices = np.linspace(0, total_points - 1, MAX_POINTS, dtype=int)
#                     reduced_points = [points[i] for i in indices]
#                 else:
#                     reduced_points = points.copy()

#                 # Pad if less than MAX_POINTS
#                 while len(reduced_points) < MAX_POINTS:
#                     reduced_points.append((0, 0, 0))

#                 reduced_points[0] = (
#                     reduced_points[0][0],
#                     reduced_points[0][1],
#                     0,
#                 )  # First point pen=0

#                 dataset.append([[int(x), int(y), int(p)] for (x, y, p) in reduced_points])

#                 try:
#                     with open("saved_strokes.json", "w") as f:
#                         json.dump(dataset, f)
#                     st.success(f"✅ Drawing saved! Total saved strokes: {len(dataset)}")
#                 except Exception as e:
#                     st.error(f"❌ Error saving drawing: {str(e)}")

# elif mode == "🔁 Replay Last":
#     if dataset:
#         last_sample = dataset[-1]
#         st.write(f"🔄 Replaying Last Drawing with {len(last_sample)} Points")

#         path_points = [(x, y, 0, 0) for x, y, _ in last_sample]

#         st_canvas(
#             fill_color="rgba(0, 0, 0, 1)",
#             stroke_width=4,
#             stroke_color="#000000",
#             background_color="#FFFFFF",
#             width=CANVAS_SIZE,
#             height=CANVAS_SIZE,
#             initial_drawing={
#                 "version": "4.4.0",
#                 "objects": [{
#                     "type": "path",
#                     "path": [(0, 0, 0, 0)] + path_points,
#                 }]
#             },
#             drawing_mode="transform",
#             key="canvas_replay",
#         )
#     else:
#         st.warning("⚠️ No saved drawing to replay.")



# ----------------------------------------------------------------------------- ( Globallay Shares Same Data )

# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# import numpy as np
# import json
# import os

# # Config
# CANVAS_SIZE = 400
# MAX_POINTS = 100
# MIN_POINTS = 80
# DATA_FILE = "saved_strokes.json"

# # Load existing data (persistent across sessions)
# if "all_data" not in st.session_state:
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as f:
#             try:
#                 st.session_state.all_data = json.load(f)
#             except json.JSONDecodeError:
#                 st.session_state.all_data = []
#     else:
#         st.session_state.all_data = []

# st.title("✍️ Hindi Numeral Stroke Recorder")

# # Drawing canvas
# canvas_result = st_canvas(
#     fill_color="rgba(0,0,0,1)",
#     stroke_width=4,
#     stroke_color="#000000",
#     background_color="#FFFFFF",
#     width=CANVAS_SIZE,
#     height=CANVAS_SIZE,
#     drawing_mode="freedraw",
#     key="canvas",
# )


# # Extract stroke points
# def extract_points(json_data):
#     points = []
#     if json_data and "objects" in json_data:
#         for obj in json_data["objects"]:
#             if obj["type"] == "path":
#                 for cmd in obj["path"]:
#                     if len(cmd) >= 3:
#                         x, y = int(cmd[1]), int(cmd[2])
#                         p = 0 if len(points) == 0 else 1
#                         points.append([x, y, p])
#     return points


# # Downsample or pad to exactly 100
# def process_points(points):
#     total = len(points)
#     if total > MAX_POINTS:
#         indices = np.linspace(0, total - 1, MAX_POINTS, dtype=int)
#         points = [points[i] for i in indices]
#     elif total < MAX_POINTS:
#         points += [[0, 0, 0]] * (MAX_POINTS - total)
#     return points


# # Display count
# st.markdown(f"📦 **Total Saved Drawings**: `{len(st.session_state.all_data)}`")

# # Save button
# if st.button("💾 Save Drawing"):
#     points = extract_points(canvas_result.json_data)

#     if len(points) < MIN_POINTS:
#         st.warning(f"⚠️ Too few points! Minimum {MIN_POINTS} required.")
#     else:
#         processed = process_points(points)
#         st.session_state.all_data.append(processed)

#         # Save to file
#         try:
#             with open(DATA_FILE, "w") as f:
#                 json.dump(st.session_state.all_data, f)
#             st.success("✅ Drawing saved successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to save drawing: {str(e)}")

# # Option to view all saved stroke data
# if st.checkbox("📋 Show All Saved Strokes"):
#     if st.session_state.all_data:
#         st.json(st.session_state.all_data)
#     else:
#         st.info("No saved strokes yet.")

# # Option to browse stroke data by index
# if st.checkbox("🔍 Browse Saved Drawing by Index"):
#     if st.session_state.all_data:
#         idx = st.slider(
#             "Select Drawing Index", 0, len(st.session_state.all_data) - 1, 0
#         )
#         st.json(st.session_state.all_data[idx])
#     else:
#         st.info("No saved strokes to browse.")

# # Clear all saved strokes
# if st.button("🧹 Clear All Saved Strokes"):
#     st.session_state.all_data = []
#     if os.path.exists(DATA_FILE):
#         os.remove(DATA_FILE)
#     st.success("✅ All saved strokes cleared.")





# -------------------------------------------------------------------------------------------------------------------( Session Based without All Stroke )


# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# import numpy as np
# import json

# # Config
# CANVAS_SIZE = 400
# MAX_POINTS = 100
# MIN_POINTS = 70

# st.title("✍️ Hindi Numeral Stroke Recorder (Session-based)")

# # Session-specific data (no shared file)
# if "session_data" not in st.session_state:
#     st.session_state.session_data = []

# # Drawing canvas
# canvas_result = st_canvas(
#     fill_color="rgba(0,0,0,1)",
#     stroke_width=4,
#     stroke_color="#000000",
#     background_color="#FFFFFF",
#     width=CANVAS_SIZE,
#     height=CANVAS_SIZE,
#     drawing_mode="freedraw",
#     key="canvas",
# )


# # Extract stroke points
# def extract_points(json_data):
#     points = []
#     if json_data and "objects" in json_data:
#         for obj in json_data["objects"]:
#             if obj["type"] == "path":
#                 for cmd in obj["path"]:
#                     if len(cmd) >= 3:
#                         x, y = int(cmd[1]), int(cmd[2])
#                         p = 0 if len(points) == 0 else 1
#                         points.append([x, y, p])
#     return points


# # Downsample or pad to exactly MAX_POINTS
# def process_points(points):
#     total = len(points)
#     if total > MAX_POINTS:
#         indices = np.linspace(0, total - 1, MAX_POINTS, dtype=int)
#         points = [points[i] for i in indices]
#     elif total < MAX_POINTS:
#         points += [[0, 0, 0]] * (MAX_POINTS - total)
#     return points


# # Display total saved drawings
# st.markdown(
#     f"📦 **Total Saved Drawings (This Session)**: `{len(st.session_state.session_data)}`"
# )

# # Save button
# if st.button("💾 Save Drawing"):
#     points = extract_points(canvas_result.json_data)
#     if len(points) < MIN_POINTS:
#         st.warning(f"⚠️ Too few points! Minimum {MIN_POINTS} required.")
#     else:
#         processed = process_points(points)
#         st.session_state.session_data.append(processed)
#         st.success("✅ Drawing saved to session!")

# # View stroke data by index
# if st.checkbox("📋 Show Saved Stroke Data by Index"):
#     if st.session_state.session_data:
#         selected_index = st.number_input(
#             "Select Drawing Index",
#             min_value=0,
#             max_value=len(st.session_state.session_data) - 1,
#             step=1,
#             value=len(st.session_state.session_data) - 1,
#         )
#         st.json(st.session_state.session_data[selected_index])
#     else:
#         st.info("No saved strokes yet.")

# # Clear button
# if st.button("🧹 Clear This Session's Strokes"):
#     st.session_state.session_data = []
#     st.success("✅ All session strokes cleared.")

# ---------------------------------------------------------------------------------------------( Before Prediction )

import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import json

# Config
CANVAS_SIZE = 400
MAX_POINTS = 100
MIN_POINTS = 70

st.title("✍️ Hindi Numeral Stroke Recorder (Session-based)")

# Session-specific data (no shared file)
if "session_data" not in st.session_state:
    st.session_state.session_data = []

# Drawing canvas
canvas_result = st_canvas(
    fill_color="rgba(0,0,0,1)",
    stroke_width=4,
    stroke_color="#000000",
    background_color="#FFFFFF",
    width=CANVAS_SIZE,
    height=CANVAS_SIZE,
    drawing_mode="freedraw",
    key="canvas",
)

# Extract stroke points
def extract_points(json_data):
    points = []
    if json_data and "objects" in json_data:
        for obj in json_data["objects"]:
            if obj["type"] == "path":
                for cmd in obj["path"]:
                    if len(cmd) >= 3:
                        x, y = int(cmd[1]), int(cmd[2])
                        p = 0 if len(points) == 0 else 1
                        points.append([x, y, p])
    return points

# Downsample or pad to exactly MAX_POINTS
def process_points(points):
    total = len(points)
    if total > MAX_POINTS:
        indices = np.linspace(0, total - 1, MAX_POINTS, dtype=int)
        points = [points[i] for i in indices]
    elif total < MAX_POINTS:
        points += [[0, 0, 0]] * (MAX_POINTS - total)
    return points

# Display total saved drawings
st.markdown(
    f"📦 **Total Saved Drawings (This Session)**: `{len(st.session_state.session_data)}`"
)

# Save button
if st.button("💾 Save Drawing"):
    points = extract_points(canvas_result.json_data)
    if len(points) < MIN_POINTS:
        st.warning(f"⚠️ Too few points! Minimum {MIN_POINTS} required.")
    else:
        processed = process_points(points)
        st.session_state.session_data.append(processed)
        st.success("✅ Drawing saved to session!")

# View stroke data by index
if st.checkbox("📋 Show Saved Stroke Data by Index"):
    if st.session_state.session_data:
        selected_index = st.number_input(
            "Select Drawing Index",
            min_value=0,
            max_value=len(st.session_state.session_data) - 1,
            step=1,
            value=len(st.session_state.session_data) - 1,
        )
        st.json(st.session_state.session_data[selected_index])
    else:
        st.info("No saved strokes yet.")

# 🔄 Show All Saved Strokes in one big list
if st.checkbox("📑 Show All Saved Stroke Data (As One List)"):
    if st.session_state.session_data:
        st.json(st.session_state.session_data)
    else:
        st.info("No saved strokes yet.")

# Clear button
if st.button("🧹 Clear This Session's Strokes"):
    st.session_state.session_data = []
    st.success("✅ All session strokes cleared.")


