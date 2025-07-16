import pygame
import core.controller as controller
from core.utils.triangleshape import TriangleShape
from core.config import PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from entities.projectile.projectile import Projectile

# TODO Give the player a triangular collision box
# TODO Add multiple lives + respawning
class Player(TriangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_HEIGHT, PLAYER_WIDTH)
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        self.turn_speed = PLAYER_TURN_SPEED
        self.move_speed = PLAYER_SPEED

    def move(self, direction):
        next_position = self.position + pygame.Vector2(0,1).rotate(self.rotation) * (self.move_speed * controller.DELTA_TIME * direction)
        
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

    # TMP
    def effectiveRadius(self):
        return self.height/2 * self.scale
        
        
