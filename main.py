import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from logger import log_event
from shot import Shot

import sys

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable) 
    Asteroid.containers = (asteroids,updatable, drawable, )
    AsteroidField.containers = (updatable,)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    Player.containers = (updatable,drawable)
    player = Player (SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    dt = 0.0
    

   
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player): 
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
       
       
       
       
        screen.fill("black")
        for bear in drawable:
            bear.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()















