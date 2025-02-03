import pygame
import Core.level as level

class World:
    def __init__(self, game) -> None:
        self.game = game
        self.level = level.Level(game)