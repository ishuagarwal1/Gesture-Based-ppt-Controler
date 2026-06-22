import numpy as np
from .image import Image

def convolve(img, kernel):
    kh, kw = kernel.shape
    pad = kh // 2
    p = np.pad(img.data, ((pad,pad),(pad,pad),(0,0)), mode='edge') if img.c > 1 else np.pad(img.data, ((pad,pad),(pad,pad)), mode='edge')
    out = np.zeros_like(img.data)

    for y in range(img.h):
        for x in range(img.w):
            if img.c > 1:
                for c in range(img.c):
                    out[y,x,c] = (p[y:y+kh, x:x+kw, c] * kernel).sum()
            else:
                out[y,x] = (p[y:y+kh, x:x+kw] * kernel).sum()

    return Image(out)
