import pygame
import level

class World:
    def __init__(self, game) -> None:
        self.game = game
        self.level = level.Level(game)