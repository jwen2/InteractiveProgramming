""" John Wen"""

import pygame
import os

pygame.init()

background_color = (255,255,255)
RED = (255,0,0)
width, height = 640, 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Plague Simulation')
screen.fill(background_color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """ circles represent classes for now"""
    pygame.draw.circle(screen, RED, (300,200),38)
    pygame.draw.circle(screen, (0,255,0), (150,250),36)
    pygame.draw.circle(screen, (0,0,255), (200,450),30)
    """ Black box will be sending you to upgrade screen"""
    pygame.draw.rect(screen, (0,0,0), [600,440,40,40])
    """Red Rectangle will display time"""
    pygame.draw.rect(screen, (RED), [300,0,600,40])
    pygame.display.update()

pygame.quit()
