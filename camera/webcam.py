import cv2

def open_webcam(camera_id=0):
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        raise RuntimeError("Cannot open webcam")
    return cap

def read_frame(cap):
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Cannot read frame from webcam")
    return frame

def release_webcam(cap):
    cap.release()
