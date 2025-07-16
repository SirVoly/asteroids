import pygame
import core.controller as controller
from core.utils.circleshape import CircleShape
from core.config import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from entities.projectile.projectile import Projectile

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        next_position = self.position + pygame.Vector2(0,1).rotate(self.rotation) * (PLAYER_SPEED * dt)
        
        # Out of Bounds: X-axis
        if next_position[0] < 0:
            next_position[0] = 0
        elif next_position[0] > controller.CURRENT_SCREEN_WIDTH:
            next_position[0] = controller.CURRENT_SCREEN_WIDTH
        
        # Out of Bounds: Y-axis
        if next_position[1] < 0:
            next_position[1] = 0
        elif next_position[1] > controller.CURRENT_SCREEN_HEIGHT:
            next_position[1] = controller.CURRENT_SCREEN_HEIGHT

        self.position = next_position

    def shoot(self, dt):
        self.shoot_cooldown -= dt
        if (self.shoot_cooldown <= 0):
            shot = Projectile(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * (PLAYER_SHOOT_SPEED)
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        
        
