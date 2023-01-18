import pygame 
from settings import * 

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((SIZE,SIZE))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 8 
        self.jump_speed = 16
        self.gravity = 0.8
        self.on_floor = True  
        self.start_pos = pos
        self.levelUp = False

    def animation(self):

        if self.on_floor == False:
            if self.direction.y > 0:
                self.image = pygame.image.load('game-aseprite/down.png').convert_alpha()
            else:
                self.image = pygame.image.load('game-aseprite/jump.png').convert_alpha()
        elif self.direction.x != 0:  
            chooser = (pygame.time.get_ticks() // 500) % 2
            img_list = ['game-aseprite/run1.png','game-aseprite/run2.png']

            if self.direction.x > 0:
                self.image = pygame.image.load(img_list[chooser]).convert_alpha()
            if self.direction.x < 0:   
                img = pygame.image.load(img_list[chooser]).convert_alpha()
                self.image = pygame.transform.flip(img,True,False)
        else:
            self.image = pygame.image.load('game-aseprite/stand.png').convert_alpha()

    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a] and self.rect.x > 0:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if key[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -self.jump_speed 

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y  

    def verticall_movement(self,tile,laser):
        for sprite in tile.sprites():
            if self.rect.colliderect(sprite.rect):
                if self.rect.y < sprite.rect.y:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top
                    self.on_floor = True 

                if self.rect.y > sprite.rect.y:
                    self.direction.y = 0
                    self.rect.top = sprite.rect.bottom

        for sprite in laser.sprites():
            if self.rect.colliderect(sprite.rect):
                if self.rect.y < sprite.rect.y:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top
                    self.on_floor = True 
                if self.rect.y > sprite.rect.y:
                    self.direction.y = 0
                    self.rect.top = sprite.rect.bottom

        self.animation()

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def horizontall_movement(self,tile,laser):
        for sprite in tile.sprites():
            if self.rect.colliderect(sprite.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right

        for sprite in laser.sprites():
            if self.rect.colliderect(sprite.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right

    def touch_laser(self,laser):
        for sprite in laser.sprites():
            for sprite in sprite.ammo.sprites():
                if self.rect.colliderect(sprite.rect):
                    self.game_over()

    def game_over(self):
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]

    def level_up(self):
        if self.rect.x > WIDTH:
            self.levelUp = True 

    def update(self,tile,laser):
        self.input()
        self.rect.x += self.direction.x * self.speed 
        self.horizontall_movement(tile,laser) 
        self.apply_gravity()
        self.verticall_movement(tile,laser)
        self.touch_laser(laser)
        self.level_up()
