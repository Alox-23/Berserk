import pygame
import player
import world
import render
import tileObj


class Game:
    def __init__(self):
        pass

    def start(self):
        pygame.init()

        self.init_vars()

        self.render = render.Render(self)
        self.player = player.Player(self)
        self.tile_obj = tileObj.TileObjects(self)
        self.world = world.World(self)
        

        self.mainloop()

    def update(self):
        self.tile_obj.update()
        self.player.update()

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.delta_time = self.clock.tick(self.fps)
            self.delta_time /= 10
            self.update()
            self.render.render()

    def init_vars(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.delta_time = 0

        self.tile_size = 16