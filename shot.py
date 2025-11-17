import pygame

from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=LINE_WIDTH)
    
    def update(self, dt):
        #print (f"position: {self.position} || velocity: {self.velocity}")
        self.position += self.velocity * dt