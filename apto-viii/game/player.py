import numpy as np


class player:
    color = (255, 0, 0)

    def __init__(self, cv):
        self.cv = cv
        self.lower_color = np.array([100, 100, 20])
        self.upper_color = np.array([125, 255, 255])

    def detectarColision(self, comida, x1, y1, w1, h1):
        x2, y2, w2, h2 = comida.x, comida.y, comida.w, comida.h
        if (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2):
            return True
        else:
            return False

    def dibujar(self, img, comidas):
        hsv = self.cv.cvtColor(img, self.cv.COLOR_BGR2HSV)
        mask = self.cv.inRange(hsv, self.lower_color, self.upper_color)
        res = self.cv.bitwise_and(img, img, mask=mask)

        contours, _ = self.cv.findContours(
            mask, self.cv.RETR_EXTERNAL, self.cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x1, y1, w1, h1 = self.cv.boundingRect(contour)
            if (w1 > 70 and h1 > 70):
                self.cv.rectangle(
                    img, (x1, y1), (x1+w1, y1+h1), self.color, -1)
                for comida in comidas:
                    choque = self.detectarColision(comida, x1, y1, w1, h1)
                    if (choque):
                        comida.color = (0, 255, 0)
                        print("Choque")


#   if (
#     rect1.x < rect2.x + rect2.w &&
#     rect1.x + rect1.w > rect2.x &&
#     rect1.y < rect2.y + rect2.h &&
#     rect1.h + rect1.y > rect2.y
#   ) {
#     // ¡colisión detectada!
#     this.color("green");
#   } else {
#     // no hay colisión
#     this.color("blue");
#   }
