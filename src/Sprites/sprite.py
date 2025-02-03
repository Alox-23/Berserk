import pygame
import os

class Sprite(pygame.sprite.Sprite):
    def __init__(self, path, *args) -> None:
        super().__init__(*args)
        self.load_animations_from_individual_sheet(path, 80)
        self.image = self.animations[self.animation_names[0]][0][0]
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)

    def update(self, delta):
        self.rect.x -= delta.x
        self.rect.y -= delta.y

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
        d.blit(self.image, self.rect)