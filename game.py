import pygame 
from settings import * 
from tile import Tile 
from player import Player 
from laser import Laser 

class Game():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.level_number = 1
        self.setup(level_dic[self.level_number])

    def setup(self,level_data):

        self.tile = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.laser = pygame.sprite.Group()

        for row_index,row in enumerate(level_data):
            for column_index,cell in enumerate(row):
                x = column_index * SIZE
                y = row_index * SIZE 

                if cell == '0':
                    tile = Tile((x,y))
                    self.tile.add(tile)

                if cell == 'P':
                    player = Player((x,y))
                    self.player.add(player)

                if cell in laser_direction.keys():
                    laser = Laser((x,y),laser_direction[cell])
                    self.laser.add(laser)


    def run(self):
        self.tile.draw(self.display_surface) 

        self.player.draw(self.display_surface)
        self.player.update(self.tile,self.laser)

        self.laser.draw(self.display_surface)
        self.laser.update(self.tile)

        if self.player.sprite.levelUp:
            self.level_number += 1
            self.setup(level_dic[self.level_number])