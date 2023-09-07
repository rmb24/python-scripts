import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    colors = {
        'blue': ([110, 50, 50], [130, 255, 255], (255, 0, 0)),
        'green': ([50, 50, 50], [70, 255, 255], (0, 255, 0)),
        'red': ([0, 50, 50], [10, 255, 255], (0, 0, 255))
    }

    for color, (lower, upper, color_bgr) in colors.items():
        mask = cv.inRange(hsv, np.array(lower), np.array(upper))
        contours = cv.findContours(
            mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

        if len(contours) > 0:
            area = max(contours, key=cv.contourArea)
            x, y, w, h = cv.boundingRect(area)
            cv.rectangle(frame, (x, y), (x+w, y+h), color_bgr, 2)

    cv.imshow('Seguimiento', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
cv.waitKey(1)
cv.waitKey(1)
cv.waitKey(1)
