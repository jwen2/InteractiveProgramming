import os
import pygame
import random
import math

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
font = pygame.font.SysFont('Consolas', 20)

class Country:
    """
    Each country has its maximum population without any inflected people,
    before we do click the country in the beginning of game.
    """
    def __init__(self, x, y, max_pop, radius=50, color=RED, infected_pop=0, infected_rate=1.1, dead_pop = 0):
        self.initial_pos = (x, y)
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.infected_pop = infected_pop
        self.infected_rate = infected_rate
        self.max_pop = max_pop
        self.dead_pop = dead_pop

    def infected_ratio(self):
        if self.max_pop != 0:
            return int(self.infected_pop) / self.max_pop
        else:
            return 1
    def death(self):
        """
        A part of infected population would be passed away.
        Then the infected population and maximum population will be reduced as many as the number of people death.
        """
        death_pop = 0
        alive_pop = self.max_pop
        if self.infected_ratio() > 0.10:
            if self.infected_pop > 10:
                death_pop = int(self.infected_pop*(random.random()/10))
            else:
                if self.max_pop >= 1:
                    death_pop = 1
                else:
                    death_pop = 0

        self.infected_pop = self.infected_pop - death_pop
        self.max_pop -= death_pop
        self.dead_pop += death_pop

    def step(self):
        """
        If infection starts (infect_pop changed into unity),
        then the infection starts with the certain rate
        """
        if self.infected_pop < self.max_pop:
            self.infected_pop = self.infected_pop * self.infected_rate
            if self.infected_pop >= self.max_pop:
                self.infected_pop = self.max_pop

        """return integer part of infected population"""
        # return int(self.infected_pop)

        """return probability"""
        return self.infected_ratio()*1.00


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

    def propagation(self, other):
        """
        The pathogen can propagate to other countries with certain probability.
        """
        if self.infected_pop >= 1 and other.infected_pop == 0:
            if random.random() <= self.infected_ratio()/10:
                other.infected_pop = 1


background_color = (255,255,255)
width, height = 640, 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Plague Simulation')
screen.fill(background_color)

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


    basicfont = pygame.font.SysFont(None, 20)
    text = basicfont.render('Welcome To A Plague Simulation! Press C to Start, Click on a country to start your infection', True, (0, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)

    pygame.display.update()

screen = pygame.display.set_mode((640, 480))

""" Herein, three countries are defined """
country1 = Country(200, 120, 200, radius=60)
country2 = Country(500, 180, 200, radius=40, color=BLUE)
country3 = Country(320, 360, 200, radius=50, color=GREEN)
countries = [country1, country2, country3]
country_pop_index = country1


Time = 0
Upgrade_Point = 0
infectionindex = 1
""" This is the counter to allow you to
click on a country and place a pathogen"""
clock = pygame.time.Clock()



running = True
while running:  # forever -- until user clicks in close box
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for country in countries:
                if country.contains_pt(pygame.mouse.get_pos()):
                    if infectionindex == 1:
                        country.infected_pop = country.infected_pop + 1
                        infectionindex = infectionindex - 1
                    country_pop_index = country
                        #print(country.infected_pop)

    """
    now our pathogen embarks on infection!
    type: step, death, propagation

    Modify Time + XXXX to modify the speed of the game.
    """
    if pygame.time.get_ticks() > (Time + 100):
        Time = pygame.time.get_ticks()
        #print ('For each country: (infected ratio, total population)', (country1.infected_ratio(),country1.max_pop), (country2.infected_ratio(),country2.max_pop), (country3.infected_ratio(),country3.max_pop))
        Total_infected = 0
        for country in countries:
            country.step()
            country.death()
            Total_infected += (country.infected_pop + country.dead_pop)
            for other in countries:
                if country != other:
                    country.propagation(other)
        Upgrade_Point = int(math.pow(1.02,Total_infected)-1)
        print (Upgrade_Point)

        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # erases screen
    for country in countries:
        country.draw()

    """
    the number of infected, dead, and total population is displayed whenever we click certain country
    """
    screen.blit(font.render('Infected:%.2d'%(country_pop_index.infected_pop) + ' ' +'Dead:%.2d'%(country_pop_index.dead_pop) + ' '+ 'Alive:%.2d'%(country_pop_index.max_pop) , True, (0, 255, 255)), (0, 440))
    pygame.display.update()  # updates real screen from staged screen

pygame.quit()
