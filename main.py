
import os
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from logger import log_event
from shot import Shot
from particle import Particle


import sys

HS_FILE = "highscore.txt" 
high_score = 0
if os.path.exists(HS_FILE):
    with open(HS_FILE, "r") as f:
        try:high_score = int(f.read())
        except ValueError:
            high_score = 0 














def main():
    global high_score
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
  

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN |pygame.SCALED)
    background_image = pygame.image.load("galaxy.jpg").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable) 
    Asteroid.containers = (asteroids,updatable, drawable, )
    AsteroidField.containers = (updatable,)
    Particle.containers = (particles, updatable, drawable)
    clock = pygame.time.Clock()
    Player.containers = (updatable,drawable)
    player = Player (SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    font = pygame.font.SysFont("Arial", 24)

    
    score = 0

    dt = 0.0
    
    def save_high_score():
        high_score
        with open("highscore.txt", "w") as f:
            f.write(str(high_score))
                

   
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        score += 20
                    elif asteroid.radius >= ASTEROID_MAX_RADIUS:
                        score += 2
                    else:
                        score += 5
                    if score > high_score:
                        high_score = score

            if asteroid.collides_with(player): 
                print(f"Score:{score}")
                print(f"Record: {high_score}")
                with open("highscore.txt", "w") as f:
                    f.write(str(high_score))
    
                print("Game over!")
                sys.exit()
                
        score_surface = font.render(f"Score:{score}", True, (255,255,255))
        high_score_surface = font.render(f"High Score:{high_score}", True, (255,255,255))

        line_spacing = score_surface.get_height() + 5
        screen.blit(background_image, (0,0))
        screen.blit(score_surface, (10,10))
        screen.blit(high_score_surface, (10, 10 + line_spacing))

        for bear in drawable:
            bear.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()















