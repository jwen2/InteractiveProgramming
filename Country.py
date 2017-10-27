import os
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

class Country:
    def __init__(self, x, y, max_pop, radius=50, color=RED, infected_pop=0, infected_rate=1.1):
        self.initial_pos = (x, y)
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.infected_pop = infected_pop
        self.infected_rate = infected_rate
        self.max_pop = max_pop

    def step(self):
        if self.infected_pop <= self.max_pop:
            self.infected_pop = self.infected_pop * self.infected_rate
            print(self.infected_pop)

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

country1 = Country(320, 240, 200, radius=80)

countries = [country1]

Time = 0
clock = pygame.time.Clock()

running = True
while running:  # forever -- until user clicks in close box
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for country in countries:
                if country.contains_pt(pygame.mouse.get_pos()):
                    if country.infected_pop == 0:
                        country.infected_pop = country.infected_pop + 1
                        print(country.infected_pop)
    if pygame.time.get_ticks() > (Time + 1000):
        Time = pygame.time.get_ticks()
        country.step()
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # erases screen
    for country in countries:
        country.draw()

    pygame.display.update()  # updates real screen from staged screen

pygame.quit()
