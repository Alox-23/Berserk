import pygame

class Speachbox:
    def __init__(self, game):
        self.game = game
        self.t_color = (0,0,1)
        self.height = 150
        self.margin_x = 40
        self.margin_y = 10
        self.c_image_margin = 10
        self.c_image_size = 130
        self.font_size = 50
        self.font = pygame.font.Font("data/assets/Fonts/font.ttf", self.font_size)
        self.image = pygame.Surface((self.game.render.screen.get_width() - self.margin_x*2, self.height))
        #self.image.set_colorkey(self.t_color)
        self.image.fill(self.t_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.margin_x, self.game.render.screen.get_height()-self.height-self.margin_y)
        self.text = "Hello, my name is grifith!\nWhat is yours?"
        self.c_image = pygame.transform.scale(pygame.image.load("data/assets/player.png"), (self.c_image_size, self.c_image_size))

    def draw(self, d):
        self.image = pygame.Surface((self.game.render.screen.get_width() - self.margin_x*2, self.height))
        #self.image.set_colorkey(self.t_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.margin_x, self.game.render.screen.get_height()-self.height-self.margin_y)
        self.c_image = pygame.transform.scale(pygame.image.load("data/assets/player.png"), (self.c_image_size, self.c_image_size))

        self.image.fill(self.t_color)
        self.image.blit(self.c_image, (self.c_image_margin, self.c_image_margin))

        for i, line in enumerate(self.text.split("\n")):
            line = self.font.render(line, 0, (255, 255, 255))
            self.image.blit(line, (self.c_image_size+self.c_image_margin*2, i*self.font_size - 2))

        d.blit(self.image, self.rect)