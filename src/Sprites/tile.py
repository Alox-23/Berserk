import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, *args):
        super().__init__(*args)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, delta):
        self.rect.x -= delta.x
        self.rect.y -= delta.y
        