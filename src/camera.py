class Camera:
    def __init__(self):
        self.capture = None

    def start(self):
        import cv2
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            raise Exception("Could not open video device")

    def stop(self):
        if self.capture is not None:
            self.capture.release()
            self.capture = None

    def read_frame(self):
        if self.capture is not None:
            ret, frame = self.capture.read()
            if not ret:
                raise Exception("Could not read frame from camera")
            return frame
        else:
            raise Exception("Camera is not started")