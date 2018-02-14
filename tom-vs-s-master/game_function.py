import pygame
import sys
from ship import Ship
from servo import *




import pygame
import time
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption("Hello World")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                action()
                print('left')
            elif event.key == pygame.K_LEFT:
                non()
                print('right')

        '''elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                flag == False
            elif event.key == pygame.K_LEFT:
                flag == False'''