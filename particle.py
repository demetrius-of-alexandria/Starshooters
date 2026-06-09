from circleshape import CircleShape
import pygame


class Particle(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, 2)
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.lifetime = 2

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()


    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius)