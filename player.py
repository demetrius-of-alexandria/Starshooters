from circleshape import CircleShape
from constants import PLAYER_RADIUS,LINE_WIDTH, PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x:float, y:float) -> None:
        super().__init__( x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.cooldown_timer = 0
        original_image = pygame.image.load("millenium_falcon").convert_alpha()
        size = PLAYER_RADIUS * 2
        self.image = pygame.transform.scale(original_image, (size, size))


    
    def draw(self,screen: pygame.Surface) -> None:
        
        rotated_ship = pygame.transform.rotate(self.image, -self.rotation + 180)
        new_rect = rotated_ship.get_rect(center = self.position)
        screen.blit(rotated_ship, new_rect.topleft)
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.cooldown_timer -= dt



    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotate_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotate_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self,):
        if self.cooldown_timer > 0:
            return
        else:
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        
        shot = Shot(self.position.x , self.position.y)
        
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED  

        

    
   
   
    