""" John Wen
Time runs in milliseconds, (1000 = 1 second)
"""

import pygame
import os


BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)

class Country():
    def __init__(self, pop_infected = 0, x, y, radius, color = RED):
        self.pop_infected = pop_infected
        self.location = (x, y)
        self.radius = radius
        self.color = color



pygame.init()

background_color = (255,255,255)
width, height = 640, 480

"""Bunch of variables"""
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Plague Simulation')
screen.fill(background_color)

UpgradeMenu = pygame.Rect(600,440,40,40)
Timelocation = pygame.Rect(400,0,600,40)
Populationlocation = pygame.Rect(0,440,300,400)
"""Timer"""
Time = 0
ActiveTime = True
font = pygame.font.SysFont('Consolas', 30)
Population = 125125
RedCirc = (300,200), 38

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """ circles represent classes for now"""
    pygame.draw.circle(screen, RED, (300,200), 38)
    pygame.draw.circle(screen, (0,255,0), (150,250),36)
    pygame.draw.circle(screen, (0,0,255), (200,350),30)
    """ Black box will be sending you to upgrade screen"""
    pygame.draw.rect(screen, (0,0,0), UpgradeMenu)
    """Time Display"""
    pygame.draw.rect(screen, (0,0,0), Timelocation)
    """Country Population Display"""
    pygame.draw.rect(screen, (0,0,0), Populationlocation)
    """timer display"""
    screen.blit(font.render(str(pygame.time.get_ticks()/1000), True, (255, 255, 255)), (400, 0))
    screen.blit(font.render(str(Population), True, (255, 255, 255)), (0, 440))

    pygame.display.update()


    if event.type == pygame.MOUSEBUTTONDOWN:
            if UpgradeMenu.collidepoint(pygame.mouse.get_pos()):
                if pygame.time.get_ticks() > (Time + 1000):
                    Time = pygame.time.get_ticks()

            # if RedCirc.collidepoint(pygame.mouse.get_pos()):
            #     if pygame.time.get_ticks() > (Time + 1000):
            #         Population = 12345
                """ Compare last time clicked"""
pygame.quit()
