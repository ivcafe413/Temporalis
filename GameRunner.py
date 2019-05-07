import sys
import logging

import pygame

from Game import Game
from GameRenderer import GameRenderer

# CONSTANTS
TARGET_FPS = 60
LOOP_MS_PF = (1 / TARGET_FPS) * 1000

class GameRunner:
    def __init__(self):
        pygame.init()

        self.game = Game()

        rendererOptions = type('', (), {})()
        rendererOptions.game = self.game
        rendererOptions.width = 800
        rendererOptions.height = 600

        self.gameRenderer = GameRenderer(rendererOptions)

        self.gameClock = pygame.time.Clock()
        self.currentTime = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def run(self):
        while True: # Eventually implement frame pausing
            self.currentTime += self.gameClock.get_time()

            self.handle_events()

            while self.currentTime >= LOOP_MS_PF:
                self.game.update() # Passing in update MS diff?
                self.currentTime -= LOOP_MS_PF
                if(self.currentTime >= LOOP_MS_PF):
                    logging.warning("Lag Frame: {0:n} over {1:n}".format(self.currentTime - LOOP_MS_PF, LOOP_MS_PF))

            self.gameRenderer.render() # Passing in leftover ticks for delta rendering?

            # Clock Frame
            fps = self.gameClock.get_fps()
            pygame.display.set_caption("FPS: {0:2f}".format(fps))
            self.gameClock.tick(TARGET_FPS)

def main():
    # Set Logging level based on config
    logging.basicConfig(level=logging.INFO)
    GameRunner().run()

if __name__ == '__main__':
    main()