import pygame
import sys
screen = pygame.display.set_mode((300,300))
color = (200,0,100)
pygame.init()
#just variable for text
font = pygame.font.Font(None,25)
text = font.render("игра",True,(0,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill((0, 200, 0))
        #draw rectangle
        pygame.draw.rect(screen,color,pygame.Rect(80,80, 150, 100))
        #draw text
        screen.blit(text,[131,126])

        #draw display
        pygame.display.flip()

