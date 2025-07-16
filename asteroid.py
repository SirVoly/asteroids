from circleshape import CircleShape
import pygame
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPEED_MULTIPLIER, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Create baby asteroids
        angle = random.uniform(20,50)
        a1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        a1.velocity = self.velocity.rotate(-angle) * ASTEROID_SPEED_MULTIPLIER

        a2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        a2.velocity = self.velocity.rotate(angle) * ASTEROID_SPEED_MULTIPLIER
        

    def update(self, dt):
        self.position += self.velocity * dt

        # Check if the asteroid is far off-screen
        # Add some padding (e.g., ASTEROID_MAX_RADIUS) to ensure it's fully off
        if (self.position.x < -ASTEROID_MAX_RADIUS or
            self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS or
            self.position.y < -ASTEROID_MAX_RADIUS or
            self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS):
            self.kill()