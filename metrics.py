import numpy as np

# ─── Eye Landmark Indices (MediaPipe Face Mesh) ────────────────
LEFT_EYE  = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33,  160, 158, 133, 153, 144]

# ─── Thresholds (calibrated for your face) ────────────────────
EAR_THRESHOLD    = 0.21   # below this = eye closing
CONSEC_FRAMES    = 20     # frames before drowsy alert triggers
NO_FACE_FRAMES   = 30     # frames before no-face warning triggers

# ─── Core Math ────────────────────────────────────────────────
def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def calculate_ear(landmarks, eye_indices, frame_w, frame_h):
    """
    EAR = (vertical1 + vertical2) / (2 * horizontal)
    Returns float rounded to 3 decimal places
    """
    p = []
    for idx in eye_indices:
        lm = landmarks[idx]
        p.append((lm.x * frame_w, lm.y * frame_h))

    vertical1  = euclidean(p[1], p[5])
    vertical2  = euclidean(p[2], p[4])
    horizontal = euclidean(p[0], p[3])

    if horizontal == 0:
        return 0.0

    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return round(ear, 3)

def get_avg_ear(landmarks, frame_w, frame_h):
    """Returns averaged EAR across both eyes"""
    left  = calculate_ear(landmarks, LEFT_EYE,  frame_w, frame_h)
    right = calculate_ear(landmarks, RIGHT_EYE, frame_w, frame_h)
    return round((left + right) / 2.0, 3), left, right