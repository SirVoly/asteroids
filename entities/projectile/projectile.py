from core.utils.circleshape import CircleShape
from core.config import PROJECTILE_RADIUS

class Projectile(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PROJECTILE_RADIUS)
        self.color = (255,0,0)