import pygame
from constants import *
from logger import log_state,log_event
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import *
import sys


def main():
    #print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT /2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    #Game Loop

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        
        screen.fill("black")
        updatable.update(dt)
        for thing in asteroids:
            if thing.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for thing in asteroids:
            for shot in shots:
                if thing.collides_with(shot):
                    log_event("asteroid_shot")
                    thing.kill()
                    shot.kill()
                
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        
        if event.type == pygame.QUIT:
            return
        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()
