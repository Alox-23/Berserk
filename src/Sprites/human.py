import Sprites.sprite as sprite
import pygame

class Human(sprite.Sprite):
    def __init__(self, game, pos, *args):
        super().__init__(game, "data/assets/Human", pos = pos, *args)
        self.rect.center = pos
        self.action = "idle"
    
    def update(self, delta):
        super().update(delta)
        self.update_animation()