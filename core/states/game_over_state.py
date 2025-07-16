import pygame
import core.controller as controller
import core.config as config

from core.states.game_state import GameState

# End Game State
class GameOverState(GameState):
    def __init__(self):
        self.name = config.STATE_GAME_OVER
        self.start_timer = 1
        self.font_title = pygame.font.SysFont(config.FONT, 74)
        self.font_message = pygame.font.SysFont(config.FONT, 36)

    def handle_input(self):
        if (self.start_timer < 0):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return config.STATE_PLAYING
            if keys[pygame.K_m]:
                return config.STATE_MENU
            if keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER] or keys[pygame.K_ESCAPE]:
                exit()
        return self.name
    
    def update(self):
        self.start_timer -= controller.DELTA_TIME
        return self.name
    
    def draw(self):
        # Rendering the screen
        controller.SCREEN.fill("black")

        # Render the title text
        text_welcome = self.font_title.render("GAME OVER!", True, (255, 255, 255))
        welcome_rect = text_welcome.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 - 100))
        controller.SCREEN.blit(text_welcome, welcome_rect)

        # Render the game score
        text_press_space = self.font_message.render(f"Score: {controller.SCORE}", True, (255, 255, 255))
        press_space_rect = text_press_space.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 - 50))
        controller.SCREEN.blit(text_press_space, press_space_rect)

        # Render the instruction texts
        text_press_space = self.font_message.render("Press R to restart the game", True, (255, 255, 255))
        press_space_rect = text_press_space.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 + 50))
        controller.SCREEN.blit(text_press_space, press_space_rect)

        text_press_space = self.font_message.render("Press M to go back to the menu", True, (255, 255, 255))
        press_space_rect = text_press_space.get_rect(center=(controller.CURRENT_SCREEN_WIDTH // 2, controller.CURRENT_SCREEN_HEIGHT // 2 + 100))
        controller.SCREEN.blit(text_press_space, press_space_rect)