import random as r


class food:
    def __init__(self, x, y, w, h, color=(0, 0, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel_y = r.randint(1, 5)
        self.color = color

    def mover(self):
        self.y += self.vel_y

    def dibujar(self, cv, img):
        cv.rectangle(img, (self.x, self.y),
                     (self.x+self.w, self.y+self.h), self.color, -1)
