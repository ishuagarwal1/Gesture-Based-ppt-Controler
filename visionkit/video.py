import cv2
from .image import Image

def webcam(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open webcam at index {index}")
    return cap

def read(cap):
    ret, frame = cap.read()
    if not ret:
        return None
    return Image(frame)
