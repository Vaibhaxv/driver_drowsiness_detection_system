import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

class FaceDetector:
    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def process(self, rgb_frame):
        """
        Returns landmarks list if face detected, else None
        """
        results = self.face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            return results.multi_face_landmarks[0].landmark
        return None

    def close(self):
        self.face_mesh.close()