import random as r


class food:
    color = (0, 0, 255)

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel_y = r.randint(1, 10)
        self.puntos = r.randint(2, 10)

    def puntoMedio(self, p1, p2):
        return ((p2 + p1)/2)

    def mover(self):
        self.y += self.vel_y

    def dibujar(self, cv, img):
        cv.rectangle(img, (self.x, self.y),
                     (self.x+self.w, self.y+self.h), self.color, -1)
        px = int(self.puntoMedio(self.x, self.x+self.w)) - 10
        py = int(self.puntoMedio(self.y, self.y+self.h))
        print(px, py)
        cv.putText(img, ""+str(self.puntos),
                   (px, py),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
