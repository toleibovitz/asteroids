import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable, shots_group)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots_group, updatable, drawable)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, PLAYER_RADIUS)
    dt = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.collision(player) == True:
                print("Game Over!")
                sys.exit()

            for shot in shots_group:
                if obj.collision(shot):
                    obj.split()

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)

        
        for obj in shots_group:
            obj.update(dt)
            obj.draw(screen)  

                
        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()