import numpy as np
from .image import Image

def difference(a, b):
    return Image(b.data - a.data)

def magnitude(diff):
    return abs(diff.data).mean()
