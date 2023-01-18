import pygame 
from settings import *

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,direction):
        super().__init__()
        self.image = pygame.Surface((SIZE,SIZE))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = direction 
        image = pygame.image.load('game-aseprite/laser.png')
        self.image = pygame.transform.rotate(image,self.direction*90)
        self.ammo = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()

    def gun(self):
        chooser = pygame.time.get_ticks()//1000 % 2

        center = SIZE/2-SIZE/12
        if chooser == 0:
            ammo = Ammo((self.rect.x+center,self.rect.y+center),self.direction)
            self.ammo.add(ammo)

    def kill_ammo(self,tile):
        for sprite in tile.sprites():
            for ammo in self.ammo.sprites():
                if sprite.rect.colliderect(ammo.rect):
                    ammo.kill()

    def update(self,tile):
        self.gun()
        self.ammo.draw(self.display_surface)
        self.ammo.update()
        self.kill_ammo(tile)

class Ammo(pygame.sprite.Sprite):
    def __init__(self,pos,direction):
        super().__init__()
        self.image = pygame.Surface((SIZE/6,SIZE/6))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.direction_decide(direction)
        self.speed = 8

    def direction_decide(self,direction):

        if direction == 0:
            self.direction.y = 1
        if direction == 1:
            self.direction.x = 1
        if direction == 2:
            self.direction.y = -1
        if direction == 3:
            self.direction.x = -1

    def apply_speed(self):
        self.rect.x += self.direction.x * self.speed 
        self.rect.y += self.direction.y * self.speed 

    def update(self):
        self.apply_speed() 