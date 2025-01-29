import pygame
import tile
import csv, sys, os

class Level:
    def __init__(self, game):
        self.game = game
        self.load_level()

    def load_level(self):
        path = "data/level1"
        layers = os.listdir(path)

        self.tile_set = {}
        tile_set_path = "data/assets/Tileset.png"
        tile_set_image = pygame.image.load(tile_set_path)

        #load tileset
        tile_counter = 0
        for y in range(0, tile_set_image.get_height(), self.game.tile_size):
            for x in range(0, tile_set_image.get_width(), self.game.tile_size):
                rect = (x, y, self.game.tile_size, self.game.tile_size)
                try:
                    self.tile_set[tile_counter] = tile_set_image.subsurface(rect)
                except:
                    print("error")

                tile_counter += 1

        for layer_path in layers:
            csv_data = csv.reader(open(path +"/"+ layer_path), delimiter=",")
            for y, row in enumerate(csv_data):
                for x, cell in enumerate(row):
                    if int(cell) != -1:
                        tile.Tile((x*self.game.tile_size, y*self.game.tile_size), self.tile_set[int(cell)], self.game.tile_obj)
        