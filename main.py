import pygame
import core.controller as controller
from entities.player.player import Player
from entities.asteroid.asteroid import Asteroid
from entities.asteroid.asteroidfield import AsteroidField
from entities.projectile.projectile import Projectile
from core.config import FPS

def main():

    pygame.init()

    screen = pygame.display.set_mode((controller.CURRENT_SCREEN_WIDTH, controller.CURRENT_SCREEN_HEIGHT))
    pygame.display.set_caption("Astroids")

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
    projectiles = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Projectile.containers = (updatable, drawable, projectiles)

    player = Player(controller.CURRENT_SCREEN_WIDTH / 2, controller.CURRENT_SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    game_running = True
    while game_running:
        # Code to check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                break
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                controller.CURRENT_SCREEN_WIDTH = event.size[0]
                controller.CURRENT_SCREEN_HEIGHT = event.size[1]
        
        # Update the entities
        updatable.update(dt)

        # Check for collision
        for a in asteroids:
            for shot in projectiles:
                if a.hasCollided(shot):
                    shot.kill()
                    a.split()
            if a.hasCollided(player):
                game_running = False
                break
        
        # Rendering the screen
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        # Measuring Ticks
        dt = clock.tick(FPS)/1000
    
    # Exit screen
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    exit_text = my_font.render('Game Over!', False, (255, 255, 255))
    text_position = exit_text.get_rect()
    text_position.center = (controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2)

    show_endscreen = True
    while show_endscreen:
        # Code to check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_endscreen = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER] or keys[pygame.K_ESCAPE]:
            show_endscreen = False
            break

        # Rendering the screen
        screen.fill("black")
        screen.blit(exit_text, text_position)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
