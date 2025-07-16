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

class MenuState(GameState):
    def __init__(self):
        self.font_title = pygame.font.SysFont('Comic Sans MS', 74)
        self.font_message = pygame.font.SysFont('Comic Sans MS', 36)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: # or keys[pygame.K_KP_ENTER] or keys[pygame.K_ESCAPE]:
            return PlayingState()
        return self
    
    def update(self):
        return self
    
    def draw(self):
        # Rendering the screen
        controller.SCREEN.fill("black")

        # Render the title text
        text_welcome = self.font_title.render("Welcome to ASTEROIDS", True, (255, 255, 255))
        welcome_rect = text_welcome.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 - 50))
        controller.SCREEN.blit(text_welcome, welcome_rect)

        # Render the instruction text
        text_press_space = self.font_message.render("Press SPACE to start", True, (255, 255, 255))
        press_space_rect = text_press_space.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 + 50))
        controller.SCREEN.blit(text_press_space, press_space_rect)
        

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

# End Game State
# TODO Add restart option
# TODO Add scoring
class GameOverState(GameState):
    def __init__(self):
        self.start_timer = 1
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.exit_text = my_font.render('Game Over!', False, (255, 255, 255))
        self.text_position = self.exit_text.get_rect()
        self.text_position.center = (controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2)

    def handle_input(self):
        if (self.start_timer < 0):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER] or keys[pygame.K_ESCAPE]:
                exit()
        return self
    
    def update(self):
        self.start_timer -= controller.DELTA_TIME
        return self
    
    def draw(self):
        # Rendering the screen
        controller.SCREEN.fill("black")
        controller.SCREEN.blit(self.exit_text, self.text_position)