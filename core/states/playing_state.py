import pygame
import core.controller as controller
import core.config as config

from core.states.game_state import GameState

from entities.player.player import Player
from entities.asteroid.asteroid import Asteroid
from entities.asteroid.asteroidfield import AsteroidField
from entities.projectile.projectile import Projectile

# Actual Game State
class PlayingState(GameState):
    def __init__(self):
        self.name = config.STATE_PLAYING

        # Reset the score
        controller.SCORE = 0

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
        return self.name
    
    def update(self):
        # Update the entities
        self.updatable.update()

        # Check for collision
        for a in self.asteroids:
            for shot in self.projectiles:
                if a.hasCollided(shot):
                    shot.kill()
                    a.split()
                    controller.SCORE += 1
            if a.hasCollided(self.player):
                return config.STATE_GAME_OVER
        
        return self.name
    
    def draw(self):
        # Rendering the screen
        controller.SCREEN.fill("black")
        for d in self.drawable:
            d.draw()