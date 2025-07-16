import random
from core.utils.circleshape import CircleShape
from core.config import ASTEROID_BASE_RADIUS, ASTEROID_SPEED_MULTIPLIER

class Asteroid(CircleShape):
    def __init__(self, x, y, scale):
        super().__init__(x, y, ASTEROID_BASE_RADIUS)
        self.scale = scale

    def split(self):
        self.kill()
        if self.scale <= 1:
            return
        
        # Create baby asteroids
        angle = random.uniform(20,50)
        a1 = Asteroid(self.position[0], self.position[1], self.scale - 1)
        a1.velocity = self.velocity.rotate(-angle) * ASTEROID_SPEED_MULTIPLIER

        a2 = Asteroid(self.position[0], self.position[1], self.scale - 1)
        a2.velocity = self.velocity.rotate(angle) * ASTEROID_SPEED_MULTIPLIER