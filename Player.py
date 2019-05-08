import pygame

from GameObject import GameObject

class Player(GameObject):
    def __init__(self, options):
        GameObject.__init__(self, options)
        self.color = options.color
        self.speed = options.speed
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

def jsonMap(do):
    do.color = (do.r, do.g, do.b)
    do.speed = do.s
    return do