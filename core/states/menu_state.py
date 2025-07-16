import pygame
import core.controller as controller
import core.config as config

from core.states.game_state import GameState

class MenuState(GameState):
    def __init__(self):
        self.name = config.STATE_MENU
        self.font_title = pygame.font.SysFont(config.FONT, 74)
        self.font_message = pygame.font.SysFont(config.FONT, 36)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return config.STATE_PLAYING
        return self.name
    
    def update(self):
        return self.name
    
    def draw(self):
        # Rendering the screen
        controller.SCREEN.fill("black")

        # Render the title text
        text_welcome = self.font_title.render("Welcome to ASTEROIDS", True, (255, 255, 255))
        welcome_rect = text_welcome.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 - 50))
        controller.SCREEN.blit(text_welcome, welcome_rect)

        # Render the instruction text
        text_press_space = self.font_message.render("Press SPACE to start", True, (255, 255, 255))
        press_space_rect = text_press_space.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 + 50))
        controller.SCREEN.blit(text_press_space, press_space_rect)