

import random
from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS,ASTEROID_MAX_RADIUS
from logger import log_event
from particle import Particle

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x, y, radius)

    
    
    def update(self, dt:float):
       self.position += self.velocity * dt




    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "black", self.position, self.radius, LINE_WIDTH)


    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            num_particles = 10
            for i in range(num_particles):
                random_angle = random.uniform(0,360)
                velocity = pygame.Vector2(0,1).rotate(random_angle)
                speed = random.uniform(50,150)
                new_particle = Particle(self.position.x, self.position.y, 2 , velocity)
                new_particle.velocity = velocity * speed
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

  