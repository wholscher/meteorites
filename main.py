import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:",SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for rock in asteroids:
            if rock.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if rock.collides_with(bullet):
                    rock.split()
                    bullet.kill()
                    log_event("asteroid_shot")
        screen.fill("black")
        for picture in drawable:
            picture.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
