import pygame 
from settings import * 
from sys import exit 

class Menu():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.gameOn = False 

        self.count = 1

    def input(self,):

        key = pygame.key.get_pressed()
        
        if key[pygame.K_SPACE]:
            if self.count == 1:
                self.gameOn = True 
            if self.count == 3:
                exit()

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            if self.count < 3:
                self.count += 1
            pygame.time.wait(125)

        if key[pygame.K_UP] or key[pygame.K_w]:
            if self.count > 1:
                self.count -= 1
            pygame.time.wait(125)

    def animation(self):
        img = pygame.image.load('game-aseprite/MENU.png')
        self.display_surface.blit(img,(WIDTH/2-225,HEIGHT/2-275))

        top = HEIGHT/2-275
        menu_dic = {1:top+68,2:top+253,3:top+448}

        pygame.draw.rect(self.display_surface,'#04ff99',(WIDTH/2-300,menu_dic[self.count],45,45))

    def run(self):
        self.input()
        self.animation()