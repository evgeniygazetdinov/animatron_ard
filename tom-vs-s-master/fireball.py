import pygame


class Fireball():
    def __init__(self):
        self.screen = screen
        self.image =pygame.image.load("images/fireball.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen_