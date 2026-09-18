import cv2
import numpy as np
import pygame

from camera   import Camera
from detector import FaceDetector
from metrics  import get_avg_ear, EAR_THRESHOLD, CONSEC_FRAMES, NO_FACE_FRAMES
from alert    import (play_alert, stop_alert,
                      draw_awake, draw_drowsy, draw_alert,
                      draw_no_face, draw_camera_error)

# ─── State Counters ────────────────────────────────────────────
eye_closed_frames = 0
no_face_frames    = 0

# ─── Init ──────────────────────────────────────────────────────
camera   = Camera(index=0)
detector = FaceDetector()

print("✅ Drowsiness Detection System Started")
print("Press Q to quit\n")

# ─── Camera Error Screen ───────────────────────────────────────
if not camera.is_opened():
    error_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    draw_camera_error(error_frame)
    cv2.imshow("Driver Drowsiness Detection", error_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit()

# ─── Main Loop ─────────────────────────────────────────────────
while True:
    ret, frame = camera.read()

    if not ret:
        error_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        draw_camera_error(error_frame)
        cv2.imshow("Driver Drowsiness Detection", error_frame)
        cv2.waitKey(1)
        continue

    frame_h, frame_w = frame.shape[:2]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ── Face Detection ─────────────────────────────────────────
    landmarks = detector.process(rgb_frame)

    if landmarks is None:
        no_face_frames += 1
        eye_closed_frames = 0
        stop_alert()

        if no_face_frames >= NO_FACE_FRAMES:
            draw_no_face(frame)
        else:
            # Brief grace period before showing warning
            cv2.putText(frame, "Detecting...", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (255, 255, 255), 2)

    else:
        no_face_frames = 0

        # ── EAR Calculation ────────────────────────────────────
        avg_ear, left_ear, right_ear = get_avg_ear(landmarks, frame_w, frame_h)

        # ── State Machine ──────────────────────────────────────
        if avg_ear < EAR_THRESHOLD:
            eye_closed_frames += 1

            if eye_closed_frames >= CONSEC_FRAMES:
                # ALERT STATE
                draw_alert(frame, avg_ear)
                play_alert()
            else:
                #  DROWSY WARNING STATE
                draw_drowsy(frame, avg_ear)
                stop_alert()
        else:
            # AWAKE STATE
            eye_closed_frames = 0
            stop_alert()
            draw_awake(frame, avg_ear)

        # ── Debug Info (bottom of frame) ───────────────────────
        cv2.putText(frame, f"L: {left_ear}  R: {right_ear}  Frames: {eye_closed_frames}",
                    (10, frame_h - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55,
                    (200, 200, 200), 1)

    # ── Show Frame ─────────────────────────────────────────────
    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Quitting...")
        break

# ─── Cleanup ───────────────────────────────────────────────────
camera.release()
detector.close()
cv2.destroyAllWindows()
pygame.quit()
print("✅ System shut down cleanly")