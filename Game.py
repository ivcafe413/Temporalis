class Game:
    def __init__(self):
        self.gameObjects = []

    def update(self):
        for o in self.gameObjects:
            o.update()