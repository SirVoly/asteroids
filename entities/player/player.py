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
    
    def draw(self):
        pygame.draw.polygon(controller.SCREEN, "white", self.triangle(), 2)

    def rotate(self, direction):
        self.rotation += PLAYER_TURN_SPEED * controller.DELTA_TIME * direction

    def move(self, direction):
        next_position = self.position + pygame.Vector2(0,1).rotate(self.rotation) * (PLAYER_SPEED * controller.DELTA_TIME * direction)
        
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

    def shoot(self):
        self.shoot_cooldown -= controller.DELTA_TIME
        if (self.shoot_cooldown <= 0):
            shot = Projectile(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * (PLAYER_SHOOT_SPEED)
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1)
        if keys[pygame.K_d]:
            self.rotate(1)
        if keys[pygame.K_w]:
            self.move(1)
        if keys[pygame.K_s]:
            self.move(-1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        
