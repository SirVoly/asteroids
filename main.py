import pygame
import core.controller as controller
from core.config import FPS
from core.gamestate import *

class Game:
    def __init__(self):
        pygame.init()

        # Create the screen
        controller.SCREEN = pygame.display.set_mode((controller.CURRENT_SCREEN_WIDTH, controller.CURRENT_SCREEN_HEIGHT))
        pygame.display.set_caption("Astroids")

        # Making sure the initial values match
        controller.CURRENT_SCREEN_WIDTH = controller.SCREEN.get_width()
        controller.CURRENT_SCREEN_HEIGHT = controller.SCREEN.get_height()

        # Setting the initial gamestate
        self.current_state = PlayingState()

        # Creating the clock
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # Measuring Ticks
            controller.DELTA_TIME = self.clock.tick(FPS)/1000

            # Code to check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Handle game quit event
                    if type(self.current_state) == PlayingState:
                        self.current_state = GameOverState()
                        continue
                    else:
                        exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                    controller.CURRENT_SCREEN_WIDTH = event.size[0]
                    controller.CURRENT_SCREEN_HEIGHT = event.size[1]

            next_state = self.current_state.handle_input()

            if next_state is None:
                raise ValueError(
                    f"State '{type(self.current_state).__name__}' update method returned None. "
                    "It must explicitly return a GameState object (e.g., 'return self' or 'return NewState()')."
                )
            elif next_state is not self.current_state:
                print(f"Transitioning from {type(self.current_state).__name__} to {type(next_state).__name__}")
                self.current_state = next_state
                continue

            next_state = self.current_state.update()
            
            if next_state is None:
                raise ValueError(
                    f"State '{type(self.current_state).__name__}' update method returned None. "
                    "It must explicitly return a GameState object (e.g., 'return self' or 'return NewState()')."
                )
            elif next_state is not self.current_state:
                print(f"Transitioning from {type(self.current_state).__name__} to {type(next_state).__name__}")
                self.current_state = next_state
                continue

            self.current_state.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
