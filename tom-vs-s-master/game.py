

import pygame
from settings import Setup
from ship import Ship
import game_function as gf
from enemy import Enemy
from palm import Palms
from palm2 import Palms2
from servo import *

def run_game():
    pygame.init()
    pygame.display.set_caption('')
    ai_settings = Setup()
    screen = pygame.display.set_mode((ai_settings.screen_width,
    ai_settings.screen_heigh))
    ship = Ship(ai_settings,screen)
    enemy = Enemy(screen)
    palm = Palms (screen)
    palm2 = Palms2(screen)


    while True:
        ship.update()
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship,enemy,palm,palm2)
        pygame.draw.line(screen, (0, 22, 222), (0, 0), (600, 600))
run_game()

