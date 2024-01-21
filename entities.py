import pygame

import uvage, random
class Cell (object):

    def __init__(self, x, y, radius, color = 'red'):
        self.color = color
        self.radius = radius
        self.gamebox = uvage.from_circle(x, y, color, radius)
        self.gamebox.speedx = (1 / radius) * 25
        self.gamebox.speedy = (1 / radius) * 25
        self.destX = random.randint(0, 800)
        self.destY = random.randint(0, 600)

    def setspeed(self, speed):
        self.gamebox.speedx = speed
        self.gamebox.speedy = speed
    def get(self):
        return self.gamebox

    def x(self):
        return self.gamebox.x

    def y(self):
        return self.gamebox.y

    def redius(self):
        return self.gamebox.radius

    def grow(self, size):
        self.radius += (size/2)
        self.gamebox = uvage.from_circle(self.x(), self.y(), self.color, self.radius)
        self.gamebox.speedx = (1 / self.radius) * 50
        self.gamebox.speedy = (1 / self.radius) * 50
    def moveup(self):
        self.gamebox.move(0, -self.gamebox.speedy)

    def movedown(self):
        self.gamebox.move(0, self.gamebox.speedy)
        
    def moveleft(self):
        self.gamebox.move(-self.gamebox.speedx, 0)

    def moveright(self):
        self.gamebox.move(self.gamebox.speedx, 0)