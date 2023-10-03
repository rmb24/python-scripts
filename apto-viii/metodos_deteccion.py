import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Cargar las imágenes
img = cv.imread('./images/leon.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
template = cv.imread('./images/leon_cara.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

# Crear la figura y las subtramas
fig, axs = plt.subplots(3, 6, figsize=(20, 10))

# Todos los 6 métodos para la comparación en una lista
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# Mostrar cada imagen en su subtrama correspondiente
for i, meth in enumerate(methods):
    img = img2.copy()
    method = eval(meth)
    # Aplicar la detección de plantilla
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # Si el método es TM_SQDIFF o TM_SQDIFF_NORMED, tomar el mínimo
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img, top_left, bottom_right, 255, 2)
    axs[0, i].imshow(res, cmap='gray')
    axs[0, i].set_title('Matching Result')
    axs[0, i].axis('off')
    axs[1, i].imshow(img, cmap='gray')
    axs[1, i].set_title('Detected Point')
    axs[1, i].axis('off')
    axs[2, i].imshow(template, cmap='gray')
    axs[2, i].set_title('Template')
    axs[2, i].axis('off')

# Mostrar la figura completa
plt.show()
