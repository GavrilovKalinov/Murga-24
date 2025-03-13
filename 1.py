import pygame
from pygame.draw import *
from pygame.color import THECOLORS


pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill(THECOLORS["white"])

pygame.draw.circle(screen, THECOLORS['yellow'], (200, 200), 120) #BODY
pygame.draw.circle(screen, THECOLORS['black'], (200, 200), 120, 1) #BODY_COVER
pygame.draw.rect(screen, THECOLORS['black'], (140,250,120,30)) #MOUTH

pygame.draw.circle(screen, THECOLORS['red'], (150, 170), 25)#EYE_LEFT
pygame.draw.circle(screen, THECOLORS['black'], (150, 170), 25, 1)#EYE_LEFT_COVER
pygame.draw.circle(screen, THECOLORS['black'], (150, 170), 10)#EYE_LEFT_MIDDLE
pygame.draw.polygon(screen, THECOLORS['black'], ((90, 81), (190, 156), (185, 166), (80, 91)))

pygame.draw.circle(screen, THECOLORS['red'], (250, 170), 20)#EYE_RIGHT
pygame.draw.circle(screen, THECOLORS['black'], (250, 170), 20, 1)#EYE_RIGHT_COVER
pygame.draw.circle(screen, THECOLORS['black'], (250, 170), 7)#EYE_RIGHT_MIDDLE
pygame.draw.polygon(screen, THECOLORS['black'], ((310, 115), (210, 150), (215, 160), (320, 125)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()