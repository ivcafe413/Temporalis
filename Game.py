import importlib
import json

import pygame

from dotmap import DotMap
from StateMachine.GameStateMachine import GameStateMachine

class Game:
    def __init__(self):
        self.gameObjects = []
        self.player = None
        self.stateMachine = GameStateMachine()

        # Initial Game State - Load array of game objects
        with open("Levels/Level1.json") as jsonFile:
            levelData = json.load(jsonFile)
            for o in levelData["gameObjects"]:
                # print('Class: ' + o['gameObjectClass'])
                do = DotMap(o)
                # print('Class: ' + do.gameObjectClass)
                module = importlib.import_module(do.gameObjectClass)
                class_ = getattr(module, do.gameObjectClass)

                no = class_(module.jsonMap(do))  # New Object from DotMapped Object
                if class_.__name__ == "Player":
                    self.player = no
                else:
                    self.gameObjects.append(no)

    # Player Actions Available (type == Key Up or Down)
    def action_left(self, type):
        # Overworld
        self.player.toggle_movement("left")

    def action_right(self, type):
        self.player.toggle_movement("right")

    def action_up(self, type):
        self.player.toggle_movement("up")

    def action_down(self, type):
        self.player.toggle_movement("down")

    def update(self):
        for o in self.gameObjects:
            o.update()
        self.player.update()
