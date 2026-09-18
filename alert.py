import cv2
import pygame
import numpy as np

# ─── Init pygame audio ─────────────────────────────────────────
pygame.mixer.init(frequency=44100, size=-16, channels=2)
pygame.init()

def _generate_beep(frequency=1000, duration=0.5, volume=0.8, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)
    wave = (wave * volume * 32767).astype(np.int16)
    stereo = np.column_stack((wave, wave))
    return pygame.sndarray.make_sound(stereo)

BEEP = _generate_beep()

# ─── Sound Control ─────────────────────────────────────────────
def play_alert():
    if not pygame.mixer.get_busy():
        BEEP.play()

def stop_alert():
    pygame.mixer.stop()

# ─── Visual Overlays ───────────────────────────────────────────
def draw_awake(frame, ear):
    h, w = frame.shape[:2]
    cv2.rectangle(frame, (0, 0), (w, h), (0, 255, 0), 4)
    cv2.putText(frame, "AWAKE", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    cv2.putText(frame, f"EAR: {ear}", (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def draw_drowsy(frame, ear):
    h, w = frame.shape[:2]
    cv2.rectangle(frame, (0, 0), (w, h), (0, 165, 255), 4)
    cv2.putText(frame, "DROWSY - STAY ALERT!", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 165, 255), 3)
    cv2.putText(frame, f"EAR: {ear}", (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def draw_alert(frame, ear):
    h, w = frame.shape[:2]
    cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 6)
    cv2.putText(frame, "ALERT! WAKE UP!", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255), 3)
    cv2.putText(frame, f"EAR: {ear}", (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def draw_no_face(frame):
    h, w = frame.shape[:2]
    cv2.rectangle(frame, (0, 0), (w, h), (0, 255, 255), 4)
    cv2.putText(frame, "NO FACE DETECTED", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 3)
    cv2.putText(frame, "Please adjust your position", (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def draw_camera_error(frame):
    h, w = frame.shape[:2]
    cv2.rectangle(frame, (0, 0), (w-1, h-1), (0, 0, 255), 6)
    cv2.putText(frame, "CAMERA ERROR", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.putText(frame, "Check your webcam connection", (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "Restart the application", (20, 125),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)