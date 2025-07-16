import pygame
import core.controller as controller
from entities.player.player import Player
from entities.asteroid.asteroid import Asteroid
from entities.asteroid.asteroidfield import AsteroidField
from entities.projectile.projectile import Projectile

# Interface
class GameState:
    def handle_input(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

# TODO Starting Menu State
class MenuState(GameState):
    def __init__(self):
        pass

    def handle_input(self):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass

# Actual Game State
class PlayingState(GameState):
    def __init__(self):
    # Create groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        AsteroidField.containers = (self.updatable)
        Projectile.containers = (self.updatable, self.drawable, self.projectiles)

        self.player = Player(controller.CURRENT_SCREEN_WIDTH / 2, controller.CURRENT_SCREEN_HEIGHT / 2)
        self.asteroidfield = AsteroidField()

    def handle_input(self):
        # Has no direct input handle, but the player class itself does.
        return self
    
    def update(self):
        # Update the entities
        self.updatable.update()

        # Check for collision
        for a in self.asteroids:
            for shot in self.projectiles:
                if a.hasCollided(shot):
                    shot.kill()
                    a.split()
            if a.hasCollided(self.player):
                return GameOverState()
        
        return self
    
    def draw(self):
        # Rendering the screen
        controller.SCREEN.fill("black")
        for d in self.drawable:
            d.draw()
        pygame.display.flip()

# End Game State
# TODO Add restart option
# TODO Add scoring
class GameOverState(GameState):
    def __init__(self):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.exit_text = my_font.render('Game Over!', False, (255, 255, 255))
        self.text_position = self.exit_text.get_rect()
        self.text_position.center = (controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER] or keys[pygame.K_ESCAPE]:
            exit()
        return self
    
    def update(self):
        return self
    
    def draw(self):
        # Rendering the screen
        controller.SCREEN.fill("black")
        controller.SCREEN.blit(self.exit_text, self.text_position)
        pygame.display.flip()