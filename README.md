# 🚗 Driver Drowsiness & Distraction Detection

A real-time computer vision system that monitors driver alertness using facial landmarks. Detects drowsiness via eye aspect ratio (EAR) and distraction via head pose estimation — triggering visual and audio alerts.

---

## Features

- **Drowsiness detection** — tracks eye closure duration using EAR
- **Distraction detection** — monitors head yaw and pitch for off-road gaze
- **Audio alerts** — beep sound via pygame when thresholds are exceeded
- **Visual overlays** — color-coded status borders and labels on the live feed
- **No-face handling** — graceful detection loss with a grace period before warning

---

## Project Structure

```
├── main.py           # Main loop — orchestrates camera, detection, and alerts
├── camera.py         # Webcam wrapper (OpenCV)
├── detector.py       # MediaPipe Face Mesh wrapper
├── metrics.py        # EAR calculation and drowsiness thresholds
├── distraction.py    # Head pose estimation and distraction logic
├── alert.py          # Audio alerts and visual overlay functions
└── requirements.txt  # Dependencies
```

---

## Requirements

- Python 3.8+
- Webcam

Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt` includes:
```
mediapipe==0.10.21
opencv-python==4.11.0
numpy==1.26.4
pygame==2.6.1
```

---

## Usage

```bash
python main.py
```

Press **Q** to quit.

---

## How It Works

### Drowsiness (EAR)
The Eye Aspect Ratio (EAR) measures how open the eyes are using 6 MediaPipe facial landmarks per eye:

```
EAR = (vertical1 + vertical2) / (2 × horizontal)
```

| State | Condition |
|---|---|
| Awake | `EAR ≥ 0.21` |
| Drowsy warning | `EAR < 0.21` for < 20 frames |
| Alert (beep) | `EAR < 0.21` for ≥ 20 frames |

### Distraction (Head Pose)
Yaw and pitch are estimated from nose, forehead, chin, and cheek landmark positions relative to face dimensions.

| State | Condition |
|---|---|
| Focused | `\|yaw\| ≤ 0.30` and `\|pitch\| ≤ 0.30` |
| Distracted (beep) | Either threshold exceeded for ≥ 20 frames |

Drowsiness takes **priority** over distraction in the state machine.

---

## Tuning

Edit thresholds in the relevant files to calibrate for different faces or lighting:

**`metrics.py`**
```python
EAR_THRESHOLD = 0.21   # Eye openness threshold
CONSEC_FRAMES = 20     # Frames before drowsy alert
NO_FACE_FRAMES = 30    # Frames before no-face warning
```

**`distraction.py`**
```python
YAW_THRESHOLD      = 0.30   # Left/right head turn
PITCH_THRESHOLD    = 0.30   # Up/down head tilt
DISTRACTION_FRAMES = 20     # Frames before distraction alert
```

---

## Known Issues

- `draw_distracted` in `alert.py` is incorrectly indented inside `draw_camera_error` — move it to the module level to fix an `ImportError` at runtime.
- `main.py` contains two complete `while` loops (the original and the updated version with distraction). Remove the first loop and keep only the second.
