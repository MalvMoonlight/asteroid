import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=LINE_WIDTH)
    
    def update(self, dt):
        #print (f"position: {self.position} || velocity: {self.velocity}")
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angel = random.uniform(20,50)          
            new_asteroid1 = Asteroid(self.position[0],self.position[1],self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid2 = Asteroid(self.position[0],self.position[1],self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, new_angel)*1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -new_angel)*1.2
