import pygame
import random

class Enemy:

    def __init__(self, x):
        self.x = x
    
        self.topLength = random.randint(1, 699)
        self.y1 = 0
        self.y2 = self.topLength + 200

        self.speed = 1

        self.imgTop = pygame.Surface((100, self.topLength))
        self.imgBottom = pygame.Surface((100, 900 - self.y2))


    def show(self, screen):
        self.x -= self.speed
        screen.blit(self.imgTop, (self.x, self.y1))
        screen.blit(self.imgBottom, (self.x, self.y2))

    def stop(self):
        self.speed = 0

    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value