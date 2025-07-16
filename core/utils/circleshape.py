import pygame
import core.controller as controller
from core.utils.shape import Shape

class CircleShape(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(controller.SCREEN, self.color, self.position, self.effectiveRadius(), 2)

    def update(self):
        self.position += self.velocity * controller.DELTA_TIME

        # Check if the item is far off-screen
        # Add some padding (e.g., radius) to ensure it's fully off
        if (self.position.x < -self.effectiveRadius() or
            self.position.x > controller.CURRENT_SCREEN_WIDTH + self.effectiveRadius() or
            self.position.y < -self.effectiveRadius() or
            self.position.y > controller.CURRENT_SCREEN_HEIGHT + self.effectiveRadius()):
            self.kill()

    def hasCollided(self, other):
        return self.position.distance_to(other.position) < (self.effectiveRadius() + other.effectiveRadius())

    def effectiveRadius(self):
        return self.radius * self.scale