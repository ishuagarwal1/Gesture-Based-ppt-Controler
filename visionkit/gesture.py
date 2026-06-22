import numpy as np

def classify(prev, curr, thresh=5):
    diff = curr.data - prev.data
    x_motion = diff.mean(axis=(0,1))[0]

    if x_motion > thresh:
        return "right"
    elif x_motion < -thresh:
        return "left"
    return None
