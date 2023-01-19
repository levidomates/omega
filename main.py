import pygame 
from settings import * 
from sys import exit
from game import Game 
from menu import Menu 

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

game = Game()
menu = Menu()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu.gameOn = False 

    screen.fill('black')
    if menu.gameOn:
        game.run()
    else:
        menu.run()
    pygame.display.update()