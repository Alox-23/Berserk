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

        self.queue = [
            [
                ["Hello my name is grifith\nWhat is yours?", "Hello Guts!"],
                pygame.transform.scale(pygame.image.load("data/assets/player.png"), (self.c_image_size, self.c_image_size))
            ],
            [
                ["Hello my name is grifith2\nWhat is yours?2", "Hello Guts!2"],
                pygame.transform.scale(pygame.image.load("data/assets/player.png"), (self.c_image_size, self.c_image_size))
            ]
        ]

        self.text = "Hello my name is grifith!\nWhat is yours?"

        self.c_image = self.queue[0][1]

    def update(self):
        print(self.queue)
        if self.queue != []:
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.margin_x, self.game.render.screen.get_height()-self.height-self.margin_y)            

            for event in self.game.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.queue[0][0].pop(0)
                        try:
                            self.queue[0][0][0]
                        except IndexError:
                            self.queue.pop(0)
                            if self.queue != []:
                                self.c_image = pygame.transform.scale(self.queue[0][1], (self.game.speachbox.c_image_size, self.game.speachbox.c_image_size))

    def draw(self, d):
        if self.queue != []:
            self.image = pygame.Surface((self.game.render.screen.get_width() - self.margin_x*2, self.height))
            #self.image.set_colorkey(self.t_color)
        
            self.render_c_image()
            self.render_text_instant()

            d.blit(self.image, self.rect)
    
    def render_c_image(self):
        self.image.fill(self.t_color)
        self.image.blit(self.c_image, (self.c_image_margin, self.c_image_margin))

    def render_text_instant(self):
        for i, line in enumerate(self.queue[0][0][0].split("\n")):
            line = self.font.render(line, 0, (255, 255, 255))
            self.image.blit(line, (self.c_image_size+self.c_image_margin*2, i*self.font_size - 2))

        