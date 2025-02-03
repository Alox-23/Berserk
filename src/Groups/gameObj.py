import pygame
import Sprites.player as player

class GameObjects(pygame.sprite.Group):
    def __init__(self, game, *args) -> None:
        super().__init__(*args)
        self.game = game

    def update(self):
        for i, sprite in enumerate(self.sprites()):
            sprite.update(self.game.player.scroll)

    def draw(self, d):
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            sprite.draw(d)