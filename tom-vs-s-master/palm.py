import pygame
from ship import Ship
class Palms():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/пальма.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def action(self):
        while True:
            if ship.moving_left_inf or ship.moving_right_inf  == True:
                self.screen_rect.left +=1
