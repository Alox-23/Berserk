import pygame
import Sprites.sprite as sprite
import math

class Player(sprite.Sprite):
    def __init__(self, game, pos = (0,0), *args) -> None:
        super().__init__(game, "data/assets/Player", pos = pos, *args)
        self.speed = 0.05
        self.movement_vector = pygame.math.Vector2(0, 0)
        self.scroll = pygame.math.Vector2(pos)
        self.world_pos = pygame.math.Vector2(pos)

        self.rect.center = (self.game.render.half_width, self.game.render.half_height)
        self.flip = False
        self.interaction = None

    def update(self, delta):
        self.movement()
        if self.interaction != None:
            for event in self.game.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.interaction.say("Hello traveler\nWhats your name?", "Greatings [NAME]", f"My name is\n{self.interaction.name}")
        self.update_rects(delta)
        self.update_animation()
        self.update_action()

    def draw(self, screen):
        #pygame.draw.rect(screen, (255,0,0), self.coll_rect)
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def update_action(self):
        if self.movement_vector.x > 0:
            self.action = "walk"
            self.animation_variant = 0
            self.flip = False
        elif self.movement_vector.x < 0:
            self.action = "walk"
            self.animation_variant = 0
            self.flip = True
        elif self.movement_vector.y > 0:
            self.action = "walk"
            self.animation_variant = 1
            self.flip = False
        elif self.movement_vector.y < 0:
            self.action = "walk"
            self.animation_variant = 2
            self.flip = False
        else:
            self.action = "idle"
    def movement(self):
        self.movement_vector.x = 0
        self.movement_vector.y = 0

        if self.game.keys[pygame.K_w]:
            self.movement_vector.y = -1
        if self.game.keys[pygame.K_a]:
            self.movement_vector.x = -1
        if self.game.keys[pygame.K_s]:
            self.movement_vector.y = 1
        if self.game.keys[pygame.K_d]:
            self.movement_vector.x = 1

        #apply speed
        self.movement_vector.y *= self.speed * self.game.delta_time
        self.movement_vector.x *= self.speed * self.game.delta_time

        self.rect.center += self.movement_vector
        self.world_pos += self.movement_vector

        if self.rect.centery > self.game.render.height-40:
            self.scroll.y = self.movement_vector.y
        elif self.rect.centery < 40:
            self.scroll.y = self.movement_vector.y
        else:
            self.scroll.y = 0

        if self.rect.centerx > self.game.render.width-70:
            self.scroll.x = self.movement_vector.x
        elif self.rect.centerx < 70:
            self.scroll.x = self.movement_vector.x
        else:
            self.scroll.x = 0