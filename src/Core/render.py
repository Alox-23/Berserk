import pygame
import random

class Render():
    def __init__(self, game,) -> None:
        self.game = game
        self.width, self.half_width = 192, 96
        self.height, self.half_height = 108, 54
        self.display_res = (self.width, self.height)
        self.scale = 5
        self.display = pygame.Surface(self.display_res)
        self.screen = pygame.display.set_mode((self.display_res[0]*self.scale, self.display_res[1]*self.scale), pygame.RESIZABLE)

    def add_scanlines(self, d):
        scanline_buffer = pygame.Surface((d.get_width(), d.get_height()))
        
        intensity = 1
        step = self.scale
        for i in range(0, scanline_buffer.get_height(), step):
            scanline_buffer.blit(d.subsurface(0, i, d.get_width(), step), (random.randint(-intensity, intensity),i))
            print(i)

        d.blit(scanline_buffer, (0,0))

        return scanline_buffer

    def render(self):
        pygame.display.set_caption(str(int(self.game.clock.get_fps())))
        
        self.display.fill((0, 0, 0))
        
        self.game.tile_obj.draw(self.display)
        self.game.game_obj.draw(self.display)

        self.screen.blit(pygame.transform.scale(self.display, (self.screen.get_width(), self.screen.get_height())), (0,0))
        #self.add_scanlines(self.screen)
        self.game.speachbox.draw(self.screen)

        pygame.display.update()
