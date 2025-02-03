import pygame
import Sprites.player as player
import Core.world as world
import Core.render as render
import Groups.tileObj as tileObj
import Groups.gameObj as gameObj
import Sprites.human as human
import random

class Game:
    def __init__(self):
        pass

    def start(self):
        pygame.init()

        self.init_vars()

        self.render = render.Render(self)
        self.player = player.Player(self)
        self.tile_obj = tileObj.TileObjects(self)
        self.game_obj = gameObj.GameObjects(self, self.player)
        self.world = world.World(self)

        self.game_obj.add(human.Human((50, 50)))

        self.mainloop()

    def update(self):
        self.tile_obj.update()
        self.game_obj.update()

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
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