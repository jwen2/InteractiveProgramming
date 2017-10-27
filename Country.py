import os
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()


class Ball:
    def __init__(self, x, y, radius=50, color=RED, infected_pop=0):
        self.initial_pos = (x, y)
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.infected_pop = infected_pop

    #def step

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)),
                           self.radius)

    def contains_pt(self, pt):
        x, y = pt
        if not self.x - self.radius < x < self.x + self.radius:
            return False
        if not self.y - self.radius < y < self.y + self.radius:
            return False
        return True


screen = pygame.display.set_mode((640, 480))

ball1 = Ball(320, 240, radius=80)

balls = [ball1]

running = True
while running:  # forever -- until user clicks in close box
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ball.contains_pt(pygame.mouse.get_pos()):
                    if ball.infected_pop == 0:
                        ball.infected_pop = ball.infected_pop + 1
                        print(ball.infected_pop)
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # erases screen
    for ball in balls:
        ball.draw()
    pygame.display.update()  # updates real screen from staged screen

pygame.quit()
