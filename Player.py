import pygame
import time

class Player:

    def __init__(self):
        self.x = 175
        self.y = 65
        self.currentSpeed = 0
        self.accel = 0.001
        self.img = pygame.image.load('images/player.png')    
    
    def show(self, screen):
        velocity = self.getVelocity()
        self.y += velocity
        screen.blit(self.img, (self.x, self.y))

    def reset(self):
        self.x = 175
        self.y = 65
        self.currentSpeed = 0
        self.accel = 0.001

    def getVelocity(self):
        self.currentSpeed += self.accel
        self.accel += 0.00007
        return self.currentSpeed

    def stop(self):
        self.accel = 0
        self.currentSpeed = 0

    def bounce(self):
        self.accel = -0.001
        self.currentSpeed = -1

    def outOfBounds(self):
        if self.y >= 840 or self.y <= -10:
            return True
        return False
