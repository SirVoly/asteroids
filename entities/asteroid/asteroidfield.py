import pygame
import random
import core.controller as controller
from entities.asteroid.asteroid import Asteroid
from core.config import ASTEROID_KINDS, ASTEROID_BASE_RADIUS, ASTEROID_SPAWN_RATE


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-(ASTEROID_BASE_RADIUS*ASTEROID_KINDS), y * controller.CURRENT_SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                controller.CURRENT_SCREEN_WIDTH + (ASTEROID_BASE_RADIUS*ASTEROID_KINDS), y * controller.CURRENT_SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * controller.CURRENT_SCREEN_WIDTH, -(ASTEROID_BASE_RADIUS*ASTEROID_KINDS)),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * controller.CURRENT_SCREEN_WIDTH, controller.CURRENT_SCREEN_HEIGHT + (ASTEROID_BASE_RADIUS*ASTEROID_KINDS)
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, size, position, velocity):
        asteroid = Asteroid(position.x, position.y, size)
        asteroid.velocity = velocity

    def update(self):
        self.spawn_timer += controller.DELTA_TIME
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            size = random.randint(1, ASTEROID_KINDS)
            self.spawn(size, position, velocity)