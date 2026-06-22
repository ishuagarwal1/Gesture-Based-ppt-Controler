import numpy as np
from .math import convolve

def edges(img):
    sx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    sy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    gx = convolve(img, sx).data
    gy = convolve(img, sy).data
    mag = (gx**2 + gy**2)**0.5
    from .image import Image
    return Image(mag)
