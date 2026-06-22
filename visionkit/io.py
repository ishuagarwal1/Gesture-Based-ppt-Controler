from PIL import Image as PILImage
import numpy as np
from .image import Image

def imread(path):
    return Image(np.array(PILImage.open(path).convert("RGB")))

def imwrite(path, img):
    PILImage.fromarray(img.data.clip(0,255).astype("uint8")).save(path)
