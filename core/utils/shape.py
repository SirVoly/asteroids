import pygame

# Base class for game objects
class Shape(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.scale = 1
        self.color = (255, 255, 255)

    def draw(self):
        # sub-classes must override
        pass

    def update(self):
        # sub-classes must override
        pass

    def hasCollided(self, other):
        # sub-classes must override
        return False
  