import pygame
import Core.speachbox as speachbox

class SpeachboxBit(speachbox.Speachbox):
    def __init__(self, game):
        super().__init__(game)
        self.counter = 0
        self.speed = 3

    def update(self):
        self.image = pygame.Surface((self.game.render.screen.get_width() - self.margin_x*2, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.margin_x, self.game.render.screen.get_height()-self.height-self.margin_y)

        if self.queue != []:
            for event in self.game.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.counter = 0
                        self.queue[0][0].pop(0)
                        try:
                            self.queue[0][0][0]
                        except IndexError:
                            self.queue.pop(0)
                            if self.queue != []:
                                self.c_image = pygame.transform.scale(self.queue[0][1], (self.game.speachbox.c_image_size, self.game.speachbox.c_image_size))
    
    def render_text(self):
        if self.queue != []:  
            for i, line in enumerate(self.queue[0][0][0].split("\n")):
                if self.counter < self.speed*len(line):
                    self.counter += 1
                else:
                    pass
                line_img = self.font.render(line[0:self.counter//self.speed], 0, (255, 255, 255))
                self.image.blit(line_img, (self.c_image_size+self.c_image_margin*2, i*self.font_size - 2))