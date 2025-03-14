import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")

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
        
    def face_detection(self, frame):
        optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = face_ref.detectMultiScale(optimized_frame, scaleFactor=1.1, minSize=(100, 100), minNeighbors=1)
        return faces

    def drawer_box(self, frame):
        for x, y, w, h in self.face_detection(self):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 225), 4)
            cv2.putText(frame, "Orang", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 225), 2)
        