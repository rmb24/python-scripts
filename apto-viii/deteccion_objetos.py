import matplotlib.pyplot as plt
import cv2 as cv

# Cargar las imágenes
img = cv.imread('./images/card_diamond.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

img2 = cv.imread('./images/diamond.png')
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

# Crear la figura y las subtramas
fig, axs = plt.subplots(2, 2)

# Mostrar la primera imagen en la subtrama superior izquierda
axs[0, 0].imshow(img)
axs[0, 0].set_title('Imagen original')

# Mostrar la segunda imagen en la subtrama superior derecha
axs[0, 1].imshow(img2)
axs[0, 1].set_title('Imagen de búsqueda')

# Realizar la búsqueda de la imagen y mostrar el resultado en la subtrama inferior izquierda
metodo = cv.TM_CCOEFF
resultado = cv.matchTemplate(img, img2, metodo)
axs[1, 0].imshow(resultado)
axs[1, 0].set_title('Resultado de la búsqueda')

# Dibujar el rectángulo en la imagen original y mostrarla en la subtrama inferior derecha
valor_min, valor_max, pos_min, pos_max = cv.minMaxLoc(resultado)
alto, ancho, colores = img2.shape
top_izquierda = pos_max
bottom_derecha = (pos_max[0] + ancho, pos_max[1] + alto)
cv.rectangle(img, top_izquierda, bottom_derecha, (255, 0, 0), 8)
axs[1, 1].imshow(img)
axs[1, 1].set_title('Imagen con rectángulo')

# Mostrar la figura
plt.show()
