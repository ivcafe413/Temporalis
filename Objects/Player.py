import pygame

from Objects.GameObject import GameObject

class Player(GameObject):
    def __init__(self, options):
        GameObject.__init__(self, options)
        self.color = options.color
        self.speed = options.speed

        # Movement Flags
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def toggle_movement(self, direction):
        if direction == 'left':
            self.moving_left = not self.moving_left
        elif direction == 'right':
            self.moving_right = not self.moving_right
        elif direction == 'up':
            self.moving_up = not self.moving_up
        elif direction == 'down':
            self.moving_down = not self.moving_down

    def update(self):
        # Movement Update
        moving = False
        if self.moving_left:
            dx = -(min(self.speed, self.left))
            moving = True
        elif self.moving_right:
            dx = min(self.speed, 800 - self.right) #
            moving = True
        if self.moving_up:
            dy = -(min(self.speed, self.top))
            moving = True
        elif self.moving_down:
            dy = min(self.speed, 600 - self.bottom)
            moving = True
            
        if not moving:
            return
            
        if not 'dx' in vars():
            dx = 0
        if not 'dy' in vars():
            dy = 0
            
        self.move(dx, dy)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

def jsonMap(do):
    do.color = (do.r, do.g, do.b)
    do.speed = do.s
    return do