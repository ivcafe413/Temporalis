import importlib
import json
from dotmap import DotMap

class Game:
    def __init__(self):
        self.gameObjects = []

        # Load array of game objects
        with open('Levels/Level1.json') as jsonFile:
            levelData = json.load(jsonFile)
            for o in levelData['gameObjects']:
                # print('Class: ' + o['gameObjectClass'])
                do = DotMap(o)
                # print('Class: ' + do.gameObjectClass)
                module = importlib.import_module(do.gameObjectClass)
                class_ = getattr(module, do.gameObjectClass)
                
                self.gameObjects.append(class_(module.jsonMap(do)))

    def update(self):
        for o in self.gameObjects:
            o.update()