

import random
from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS,ASTEROID_MAX_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x, y, radius)

    
    
    def update(self, dt:float):
       self.position += self.velocity * dt 




    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_vector_1 = self.velocity.rotate(angle)
        new_vector_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_vector_1 * 1.2
        
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = new_vector_2 * 1.2

  