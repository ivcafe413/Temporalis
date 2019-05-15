import pygame

from Objects.GameObject import GameObject

class Solid(GameObject):
    def __init__(self, options):
        GameObject.__init__(self, options)
        self.color = options.color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

def jsonMap(do):
    do.color = (do.r, do.g, do.b)
    return do