import numpy as np

class Image:
    def __init__(self, data):
        self.data = data.astype("float32")
        self.h, self.w = data.shape[:2]
        self.c = 1 if data.ndim == 2 else data.shape[2]

    def gray(self):
        if self.c == 1:
            return self
        g = self.data.mean(axis=2)
        return Image(g)
