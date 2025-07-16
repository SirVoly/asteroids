import pygame
import controller
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()

    screen = pygame.display.set_mode((controller.CURRENT_SCREEN_WIDTH, controller.CURRENT_SCREEN_HEIGHT))
    # Making sure the initial values match
    controller.CURRENT_SCREEN_WIDTH = screen.get_width()
    controller.CURRENT_SCREEN_HEIGHT = screen.get_height()

    # Add FPS and timing mechanics
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(controller.CURRENT_SCREEN_WIDTH / 2, controller.CURRENT_SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        # Code to check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                controller.CURRENT_SCREEN_WIDTH = event.size[0]
                controller.CURRENT_SCREEN_HEIGHT = event.size[1]
            
        updatable.update(dt)

        for a in asteroids:
            for shot in shots:
                if a.hasCollided(shot):
                    shot.kill()
                    a.split()
            if a.hasCollided(player):
                print("Game over!")
                exit()
        
        # Rendering the screen
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        # Measuring Ticks
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
