import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.image = pygame.image.load('images/r2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right_inf = False
        self.moving_left_inf = False
        self.moving_up = False
        self.moving_down = False
        self.center = float(self.rect.centerx)
        self.ai_settings = ai_settings


#draw in center bottom display
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
#add inf keys
    def update(self):
        if self.moving_right_inf:
            self.rect.centerx += 1
        if self.moving_left_inf:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -=1
        if self.moving_down:
            self.rect.centery += 1

        if self.moving_right_inf :
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left_inf:
            self.center -= self.ai_settings.ship_speed_factor
    def blitme(self):
        self.screen.blit(self.image,self.rect)

