from .video import webcam, read
from .gesture import classify
from .slides import open_ppt, next_slide, prev_slide
import time

def present(ppt_path):
    open_ppt(ppt_path)

    cap = webcam()
    prev = read(cap)

    print("Presentation started. Use gestures.")

    last_gesture_time = 0
    cooldown = 1 

    while True:
        curr = read(cap)
        if curr is None:
            break

        g = classify(prev, curr)
        current_time = time.time()

        if g == "right" and (current_time - last_gesture_time) > cooldown:
            next_slide()
            last_gesture_time = current_time

        elif g == "left" and (current_time - last_gesture_time) > cooldown:
            prev_slide()
            last_gesture_time = current_time

        prev = curr
