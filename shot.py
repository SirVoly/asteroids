import pygame
import controller
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        # Check if the asteroid is far off-screen
        # Add some padding (e.g., ASTEROID_MAX_RADIUS) to ensure it's fully off
        if (self.position.x < -SHOT_RADIUS or
            self.position.x > controller.CURRENT_SCREEN_WIDTH + SHOT_RADIUS or
            self.position.y < -SHOT_RADIUS or
            self.position.y > controller.CURRENT_SCREEN_HEIGHT + SHOT_RADIUS):
            self.kill()