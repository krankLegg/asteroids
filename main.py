import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Game init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()    
    running = True
    dt = 0

    # Player init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    # Asteroid init
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # Asteroid Field
    AsteroidField.containers = (updatable,)
    asteroidField = AsteroidField()

    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
