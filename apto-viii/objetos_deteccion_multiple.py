import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Cargar las imágenes
img_rgb = cv.imread('./images/card_diamond.png')
assert img_rgb is not None, "file could not be read, check with os.path.exists()"
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('./images/diamond.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"

# Cambiar el tamaño de la imagen de la plantilla si es necesario
if template.shape[0] > img_gray.shape[0] or template.shape[1] > img_gray.shape[1]:
    template = cv.resize(template, (img_gray.shape[1], img_gray.shape[0]))

w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.5
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
cv.imwrite('./images/res.png', img_rgb)
