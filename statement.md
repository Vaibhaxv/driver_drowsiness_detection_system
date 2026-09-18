# Problem Statement

Driver drowsiness and distraction are major safety concerns, as reduced
alertness or loss of attention can significantly increase the risk of
road accidents. Drivers may become drowsy due to fatigue, lack of sleep,
or long driving periods, while distraction can occur when the driver
looks away from the road.

This project aims to develop a real-time computer vision system that
monitors a driver's facial features through a webcam to identify signs
of drowsiness and distraction. The system uses facial landmarks to
calculate the Eye Aspect Ratio (EAR) for detecting prolonged eye closure
and estimates head pose using yaw and pitch to identify when the driver
is looking away from the road. When predefined thresholds are exceeded,
the system provides visual and audio alerts to warn the driver.

# Scope of the Project

The project focuses on real-time detection of two major driver-alertness
conditions:

-   **Drowsiness detection:** Uses Eye Aspect Ratio (EAR) to monitor eye
    closure and identify prolonged periods of closed eyes.
-   **Distraction detection:** Uses head pose estimation to detect
    excessive left/right head turns or upward/downward head tilts.
-   **Real-time monitoring:** Processes the webcam feed continuously
    while the driver is being monitored.
-   **Alert mechanism:** Provides audio beeps and visual overlays when
    drowsiness or distraction is detected.
-   **No-face handling:** Handles temporary loss of face detection with
    a grace period before issuing a warning.
-   **Threshold tuning:** Detection thresholds can be adjusted for
    different users and lighting conditions.

The current implementation is intended as a computer-vision-based driver
assistance prototype and requires a webcam and Python environment.

# Target Users

The primary target users are:

-   **Vehicle drivers** who want an additional alert system for fatigue
    and distraction.
-   **Fleet operators** who want to improve driver attentiveness and
    safety.
-   **Transportation and logistics organizations** interested in
    driver-monitoring solutions.
-   **Researchers and students** working on computer vision, facial
    landmark detection, and driver-safety systems.
-   **Developers** who want to build or extend real-time
    driver-monitoring applications.

# High-Level Features

-   **Real-time drowsiness detection** using Eye Aspect Ratio (EAR).
-   **Real-time distraction detection** using head yaw and pitch
    estimation.
-   **Audio alerts** using Pygame when drowsiness or distraction
    thresholds are exceeded.
-   **Visual status overlays** with labels and color-coded indicators on
    the live camera feed.
-   **No-face detection handling** with a configurable grace period.
-   **Configurable detection thresholds** for eye openness, head
    movement, and required consecutive frames.
-   **Webcam-based monitoring** using OpenCV and MediaPipe Face Mesh.
-   **Priority-based alert state handling**, where drowsiness takes
    priority over distraction.
