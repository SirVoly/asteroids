from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        # # Check if the asteroid is far off-screen
        # # Add some padding (e.g., ASTEROID_MAX_RADIUS) to ensure it's fully off
        # if (self.position.x < -ASTEROID_MAX_RADIUS or
        #     self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS or
        #     self.position.y < -ASTEROID_MAX_RADIUS or
        #     self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS):
        #     self.kill()