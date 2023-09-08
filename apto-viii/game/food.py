import random as r


class food:
    color = (0, 0, 255)

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # self.vel_y = r.randint(1, 2)
        self.vel_y = 0

    def mover(self):
        self.y += self.vel_y

    def dibujar(self, cv, img):
        cv.rectangle(img, (self.x, self.y),
                     (self.x+self.w, self.y+self.h), self.color, -1)
