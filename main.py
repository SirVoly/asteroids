import pygame
import core.controller as controller
import core.config as config
from core.config import FPS
from core.states.menu_state import MenuState
from core.states.playing_state import PlayingState
from core.states.game_over_state import GameOverState

class Game:
    def __init__(self):
        pygame.init()

        # States
        self.state_classes = {
            config.STATE_MENU: MenuState,
            config.STATE_PLAYING: PlayingState,
            config.STATE_GAME_OVER: GameOverState,
        }

        # Create the screen
        controller.SCREEN = pygame.display.set_mode((controller.CURRENT_SCREEN_WIDTH, controller.CURRENT_SCREEN_HEIGHT))
        pygame.display.set_caption("Astroids")

        # Making sure the initial values match
        controller.CURRENT_SCREEN_WIDTH = controller.SCREEN.get_width()
        controller.CURRENT_SCREEN_HEIGHT = controller.SCREEN.get_height()

        # Setting the initial gamestate
        self.current_state = self.state_classes[config.STATE_MENU]()

        # Creating the clock
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # Measuring Ticks
            controller.DELTA_TIME = self.clock.tick(FPS)/1000

            # Code to check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Handle game quit event
                    if self.current_state.name == config.STATE_PLAYING:
                        self.current_state = self.state_classes[config.STATE_GAME_OVER]()
                        continue
                    else:
                        exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                    controller.CURRENT_SCREEN_WIDTH = event.size[0]
                    controller.CURRENT_SCREEN_HEIGHT = event.size[1]

            next_state = self.current_state.handle_input()

            if next_state is None or not isinstance(next_state, str):
                raise ValueError(
                    f"State '{self.current_state.name}' handle_input method returned None. "
                    "It must explicitly return a string  (e.g., 'return self.name' or 'return config.STATE_...')."
                )
            elif next_state is not self.current_state.name:
                print(f"Transitioning from {self.current_state.name} to {next_state}")
                self.current_state = self.state_classes[next_state]()
                continue

            next_state = self.current_state.update()
            
            if next_state is None or not isinstance(next_state, str):
                raise ValueError(
                    f"State '{self.current_state.name}' update method returned None. "
                    "It must explicitly return a string  (e.g., 'return self.name' or 'return config.STATE_...')."
                )
            elif next_state is not self.current_state.name:
                print(f"Transitioning from {self.current_state.name} to {next_state}")
                self.current_state = self.state_classes[next_state]()
                continue

            self.current_state.draw()
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
