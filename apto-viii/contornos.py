import cv2 as cv

# Cargar imagen
img = cv.imread('img/tigre.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgGray, 127, 255, 0)
countours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, countours, -1, (0, 255, 0), 3)

cv.imshow('Imagen', img)

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)
cv.waitKey(1)
cv.waitKey(1)
