import sprite
import pygame

class Human(sprite.Sprite):
    def __init__(self, pos, *args):
        super().__init__("data/assets/Human", *args)
        self.rect.center = pos
    
    def update(self, delta):
        super().update(delta)
        self.update_animation()