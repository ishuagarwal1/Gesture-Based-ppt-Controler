import numpy as np
from .math import convolve

def blur(img):
    k = np.ones((3,3)) / 9
    return convolve(img, k)

def sharpen(img):
    k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    return convolve(img, k)
