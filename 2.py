import pygame
from pygame.draw import *
from pygame.color import THECOLORS

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill(THECOLORS['white'])

def screen_color():
    pygame.draw.rect(screen, THECOLORS['darkgoldenrod'], (0, 175, 400, 225))
    pygame.draw.rect(screen, THECOLORS['saddlebrown'], (0, 0, 400, 175))

screen_color()

def window():
    pygame.draw.rect(screen, THECOLORS['powderblue'], (250, 15, 140, 145))
    pygame.draw.rect(screen, THECOLORS['mediumturquoise'], (260, 20, 55, 30))
    pygame.draw.rect(screen, THECOLORS['mediumturquoise'], (330, 20, 55, 30))
    pygame.draw.rect(screen, THECOLORS['mediumturquoise'], (260, 60, 55, 90))
    pygame.draw.rect(screen, THECOLORS['mediumturquoise'], (330, 60, 55, 90))

window()

def wool():
    pygame.draw.ellipse(screen, THECOLORS['silver'], (200, 300, 90, 70))
    pygame.draw.ellipse(screen, THECOLORS['black'], (200, 300, 90, 70), 1)
    pygame.draw.lines(screen, THECOLORS['black'], False, [(245, 310), (257, 316), (261, 317),
    (263, 321), (274, 345)])
    pygame.draw.lines(screen, THECOLORS['black'], False, [(238, 318), (250, 324), (254, 325),
    (256, 329), (267, 353)])
    pygame.draw.lines(screen, THECOLORS['black'], False, [(210, 325), (216, 337), (217, 341),
    (221, 343), (235, 354)])
    pygame.draw.lines(screen, THECOLORS['silver'], False, (((202, 350), (190, 355), (165, 351),
    (150,355), (145, 350), (135, 352))))

wool()

pygame.draw.ellipse(screen, THECOLORS['sienna'], (280, 205, 200, 50)) #TAIL
pygame.draw.ellipse(screen, THECOLORS['black'], (280, 205, 200, 50), 1)

pygame.draw.ellipse(screen, THECOLORS['sienna'], (100, 185, 250, 80))#BODY
pygame.draw.ellipse(screen, THECOLORS['black'], (100, 185, 250, 80), 1)

pygame.draw.ellipse(screen, THECOLORS['sienna'], (250, 220, 100, 60))#LEG_LEFT_1
pygame.draw.ellipse(screen, THECOLORS['black'], (250, 220, 100, 60), 1)

pygame.draw.ellipse(screen, THECOLORS['sienna'], (325, 255, 40, 60))#LEG_LEFT_2
pygame.draw.ellipse(screen, THECOLORS['black'], (325, 255, 40, 60), 1)

pygame.draw.ellipse(screen, THECOLORS['sienna'], (100, 235, 80, 40))#LEG_RIGHT_1
pygame.draw.ellipse(screen, THECOLORS['black'], (100, 235, 80, 40), 1)

pygame.draw.ellipse(screen, THECOLORS['sienna'], (60, 215, 40, 40))#LEG_RIGHT_2
pygame.draw.ellipse(screen, THECOLORS['black'], (60, 215, 40, 40), 1)

pygame.draw.ellipse(screen, THECOLORS['sienna'], (40, 180, 120, 60))#HEAD
pygame.draw.ellipse(screen, THECOLORS['black'], (40, 180, 120, 60), 1)

pygame.draw.polygon(screen, THECOLORS['sienna'], ((120, 185), (150, 205), (150, 175)))
pygame.draw.polygon(screen, THECOLORS['black'], ((120, 185), (150, 205), (150, 175)), 1)
pygame.draw.polygon(screen, THECOLORS['silver'], ((120, 185), (150, 205), (150, 175)))
pygame.draw.polygon(screen, THECOLORS['black'], ((120, 185), (150, 205), (150, 175)), 1)

pygame.draw.polygon(screen, THECOLORS['sienna'], ((80, 185), (50, 205), (50, 175)))
pygame.draw.polygon(screen, THECOLORS['black'], ((80, 185), (50, 205), (50, 175)), 1)
pygame.draw.polygon(screen, THECOLORS['silver'], ((80, 185), (50, 205), (50, 175)))
pygame.draw.polygon(screen, THECOLORS['black'], ((80,185), (50, 205), (50, 175)), 1)

pygame.draw.polygon(screen, THECOLORS['black'], ((94, 215), (104, 215), (99, 220)))

pygame.draw.lines(screen, THECOLORS['black'], False, ((99, 220), (99,225)))

pygame.draw.lines(screen, THECOLORS['black'], False, ((99, 225), (105,229), (110, 225)))
pygame.draw.lines(screen, THECOLORS['black'], False, ((99, 225), (93,229), (88, 225)))

pygame.draw.ellipse(screen, THECOLORS['blue'], (105, 190, 35, 30))
pygame.draw.ellipse(screen, THECOLORS['black'], (105, 190, 35, 30), 1)
pygame.draw.ellipse(screen, THECOLORS['black'], (120, 190, 10, 30))
pygame.draw.ellipse(screen, THECOLORS['white'], (108, 190, 15, 10))

pygame.draw.ellipse(screen, THECOLORS['blue'], (60, 190, 35, 30))
pygame.draw.ellipse(screen, THECOLORS['black'], (60, 190, 35, 30), 1)
pygame.draw.ellipse(screen, THECOLORS['black'], (75, 190, 10, 30))
pygame.draw.ellipse(screen, THECOLORS['white'], (64, 190, 15, 10))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit() 