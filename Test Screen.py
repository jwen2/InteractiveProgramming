import pygame


background_color = (255,255,255)
RED = (255,0,0)
width, height = 640, 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Plague Simulation')
screen.fill(background_color)

pygame.init()

intro = True

while intro:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                intro = False
                running = True
            if event.key == pygame.K_q:
                pygame.quit()
                quit()


    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render('Welcome To A Plague Simulation!', True, (0, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)

    pygame.display.update()

running = True
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    """ circles represent classes for now"""
    pygame.draw.circle(screen, RED, (300,200), 38)
    pygame.draw.circle(screen, (0,255,0), (150,250),36)
    pygame.draw.circle(screen, (0,0,255), (200,350),30)

    pygame.display.update()

# import os
# import pygame
#
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
#
# pygame.init()
# font = pygame.font.SysFont('Consolas', 30)
#
# class Ball:
#     def __init__(self, x, y, radius=50, color=RED, infected_pop=0, population=2000):
#         self.initial_pos = (x, y)
#         self.x = x
#         self.y = y
#         self.color = color
#         self.radius = radius
#         self.infected_pop = infected_pop
#         self.population = population
#
#     #def step
#
#     def draw(self):
#         pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)),
#                            self.radius)
#
#     def contains_pt(self, pt):
#         x, y = pt
#         if not self.x - self.radius < x < self.x + self.radius:
#             return False
#         if not self.y - self.radius < y < self.y + self.radius:
#             return False
#         return True
#
#
# screen = pygame.display.set_mode((640, 480))
# display = 0
#
# ball1 = Ball(320, 240, radius=80)
#
# balls = [ball1]
#
# running = True
# while running:  # forever -- until user clicks in close box
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             for ball in balls:
#                 if ball.contains_pt(pygame.mouse.get_pos()):
#                     if ball.infected_pop == 0:
#                         ball.infected_pop = ball.infected_pop + 1
#                         print(ball.infected_pop)
#                     display = (ball.population)
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill(BLACK)  # erases screen
#     for ball in balls:
#         ball.draw()
#     screen.blit(font.render('Total Population:%.2d'%(display) , True, (0, 255, 255)), (0, 440))
#     pygame.display.update()  # updates real screen from staged screen
#
# pygame.quit()
