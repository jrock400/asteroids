import pygame
from circleshape import CircleShape
from constants import *
from logger import log_state,log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

        

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        #self.velocity.rotate(random_angle)bootdev run 09dc2ef8-bac4-43b1-81ff-23727cc512f6
        #self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius) 
        asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2.velocity = self.velocity.rotate(random_angle * -1) * 1.2

        
    
    