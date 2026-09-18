import cv2

class Camera:
    def __init__(self, index=0):
        self.index = index
        self.cap = cv2.VideoCapture(index)

    def is_opened(self):
        return self.cap.isOpened()

    def read(self):
        """Returns (success, frame)"""
        ret, frame = self.cap.read()
        return ret, frame

    def release(self):
        self.cap.release()