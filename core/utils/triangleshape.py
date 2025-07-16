import pygame
import core.controller as controller
from core.utils.shape import Shape

class TriangleShape(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width
        self.rotation = 0
        self.turn_speed = 1
        self.move_speed = 1

    def draw(self):
        pygame.draw.polygon(controller.SCREEN, self.color, self.triangle(), 2)

    def update(self):
        pass

    def hasCollided(self, other):
        # TODO
        return False 
    
    def triangle(self):
        # First, define the triangle in local coordinates (no rotation)
        tip = pygame.Vector2(0, self.height / 2)
        bottom_left = pygame.Vector2(-self.width / 2, -self.height / 2)
        bottom_right = pygame.Vector2(self.width / 2, -self.height / 2)

        # Rotate
        tip = tip.rotate(self.rotation)
        bottom_left = bottom_left.rotate(self.rotation)
        bottom_right = bottom_right.rotate(self.rotation)

        # Finally, translate to world position
        tip = self.position + tip
        bottom_left = self.position + bottom_left
        bottom_right = self.position + bottom_right

        return [tip, bottom_left, bottom_right]
    
    def rotate(self, direction):
        self.rotation += self.turn_speed * controller.DELTA_TIME * direction
    
    def move(self, direction):
        self.position += pygame.Vector2(0,1).rotate(self.rotation) * (self.move_speed * controller.DELTA_TIME * direction)
