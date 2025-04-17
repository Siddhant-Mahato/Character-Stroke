import numpy as np

def preprocess_strokes(strokes, max_len=100):
    all_points = []
    for stroke in strokes:
        for i, pt in enumerate(stroke):
            all_points.append([pt[0], pt[1], 0 if i < len(stroke)-1 else 1])

    all_points = np.array(all_points, dtype=np.float32)

    # Normalize
    if len(all_points) > 0:
        all_points[:, 0] -= np.min(all_points[:, 0])
        all_points[:, 1] -= np.min(all_points[:, 1])
        max_val = max(np.max(all_points[:, 0]), np.max(all_points[:, 1]))
        if max_val > 0:
            all_points[:, 0:2] /= max_val

    # Pad or truncate
    if len(all_points) < max_len:
        pad = np.zeros((max_len - len(all_points), 3))
        all_points = np.vstack([all_points, pad])
    else:
        all_points = all_points[:max_len]

    return all_points.flatten()
