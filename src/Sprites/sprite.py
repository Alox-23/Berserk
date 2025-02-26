import pygame
import os

class Sprite(pygame.sprite.Sprite):
    def __init__(self, game, path, pos = (50, 50), *args) -> None:
        super().__init__(*args)
        self.game = game

        self.load_animations_from_individual_sheet(path, 80)
        self.image = self.animations[self.animation_names[0]][0][0]
        self.c_image = pygame.image.load("data/assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

        self.coll_rect = pygame.Rect(pos, (15, 15))

        self.player_interaction = False
        self.name = "sprite"

    def check_interaction_player(self):
        if self.coll_rect.colliderect(self.game.player.coll_rect):
            self.game.player.interaction = self
            return True
        else:
            if self.game.player.interaction == self:
                self.game.player.interaction = None
            return False

    def update(self, delta):
        self.update_rects(delta)
        self.check_interaction_player()

    def say(self, *phrases):
        self.game.speachbox.queue.append([[*phrases], self.c_image])

    def update_rects(self, delta):
        self.rect.x -= delta.x
        self.rect.y -= delta.y
        self.coll_rect.center = self.rect.center

    def load_animations_from_individual_sheet(self, path, frame_size):
        self.create_animation_variables(path)        
        path = path
        frame_size = frame_size
        #go through animations sheet names
        for animation_sheet_name in self.animation_names:

            #load animation sheet image
            animation_sheet_image = pygame.image.load(path + "/" + animation_sheet_name+ ".png")
            animation_variants = []

            #go through the rows in loaded animation sheet image
            for y in range(0, animation_sheet_image.get_height(), frame_size):

                animation_frames = []

                #go through each animation frame and add it to animation_frames
                for x in range(0, animation_sheet_image.get_width(), frame_size):

                    rect = (x, y, frame_size, frame_size)

                    try:
                        animation_frames.append(animation_sheet_image.subsurface(rect))
                    except:
                        print("error")

                #add animation frames to animation variant
                animation_variants.append(animation_frames)

            #add animation variant to animation dictionary
            self.animations[animation_sheet_name] = animation_variants

    def create_animation_variables(self, path):
        self.animation_names = os.listdir(path)
        for i in range(len(self.animation_names)):
            self.animation_names[i] = self.animation_names[i][:-4]
        self.animations = {}
        self.animation_cooldown = 100
        self.animation_timer = pygame.time.get_ticks()
        self.action = self.animation_names[2]
        self.animation_frame = 0
        self.animation_variant = 0

    def update_animation(self):
        try:
            self.image = self.animations[self.action][self.animation_variant][self.animation_frame]
            if pygame.time.get_ticks() - self.animation_timer > self.animation_cooldown:
                self.animation_frame += 1
                self.animation_timer = pygame.time.get_ticks()

            if self.animation_frame > len(self.animations[self.action][self.animation_variant])-1:
                self.animation_frame = 0
        except:
            self.animation_frame = 0

    def draw(self, d):
        #pygame.draw.rect(d, (0,0,255), self.coll_rect)
        d.blit(self.image, self.rect)
        if self.game.player.interaction == self:
            pygame.draw.rect(d, (50,50,200), pygame.Rect(self.coll_rect.centerx-2, self.coll_rect.y-2, 4, 1))
            