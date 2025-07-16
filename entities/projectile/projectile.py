import pygame
import core.controller as controller
from core.utils.circleshape import CircleShape
from core.config import PROJECTILE_RADIUS

class Projectile(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PROJECTILE_RADIUS)

    def draw(self):
        pygame.draw.circle(controller.SCREEN, "red", self.position, self.radius, 2)

    def update(self):
        self.position += self.velocity * controller.DELTA_TIME

        # Check if the asteroid is far off-screen
        # Add some padding (e.g., ASTEROID_MAX_RADIUS) to ensure it's fully off
        if (self.position.x < -PROJECTILE_RADIUS or
            self.position.x > controller.CURRENT_SCREEN_WIDTH + PROJECTILE_RADIUS or
            self.position.y < -PROJECTILE_RADIUS or
            self.position.y > controller.CURRENT_SCREEN_HEIGHT + PROJECTILE_RADIUS):
            self.kill()