import os
import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
font = pygame.font.SysFont('Consolas', 20)

class Country:
    """
    Each country has its maximum population without any infected people,
    before we click the country in the beginning of the game.
    """
    def __init__(self, x, y, max_pop, radius=50, color=RED, infected_pop=0, infected_rate=1.1, dead_pop=0, death_rate=1, airborne_rate=0):
        self.initial_pos = (x, y)
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.infected_pop = infected_pop
        self.infected_rate = infected_rate
        self.max_pop = max_pop
        self.dead_pop = dead_pop
        self.death_rate = death_rate
        self.airborne_rate = airborne_rate

    def infected_ratio(self):
        if self.max_pop != 0:
            return int(self.infected_pop) / self.max_pop
        else:
            return 1

    def death(self):
        """
        A part of the infected population would be passed away.
        Then the infected population and maximum population will be reduced as many as the number of people death.
        """
        death_pop = 0
        alive_pop = self.max_pop
        if self.infected_ratio() > 0.10:
            if self.infected_pop > 10:
                death_pop = int(self.death_rate*self.infected_pop*(random.random()/15))
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
        return self.infected_ratio()


    def draw(self):
        """ draws the location of the country as a circle """
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)),
                           self.radius)

    def contains_pt(self, pt):
        """ countains points function to see if mouseclicks are
        within the circles of the country """
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
    """ Intro of the game gives the intro screen with
    upgrade instructions as well as how to start the game """

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
    """ Renders the text where it tells the user to
    press c to start the game, and gives instructions on how to upgrade the game"""

    basicfont = pygame.font.SysFont(None, 20)
    text = basicfont.render('Welcome To A Plague Simulation! Press C to Start, Click on a country to start your infection', True, (0, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)
    screen.blit(basicfont.render('For Upgrades, Press I to increase infection rate, K to increase kill rate, and A to increase airborne rate' , True, (0, 0, 0), (255, 255, 255)), (0, 300 ))

    pygame.display.update()

screen = pygame.display.set_mode((640, 480))

""" Herein, three countries are defined """
country1 = Country(200, 120, 200, radius=60)
country2 = Country(500, 180, 200, radius=40, color=BLUE)
country3 = Country(320, 360, 200, radius=50, color=GREEN)
countries = [country1, country2, country3]
country_pop_index = country1
total_pop = 0

Time = 0
time = 0
Upgrade_Point = 0
infectionindex = 1
""" This is the counter to allow you to
click on a country and place a pathogen"""
clock = pygame.time.Clock()

upgrades = 0

""" Pressing C will officially start the game running our
game function with time"""

running = True
while running:  # forever -- until user clicks in close box
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for country in countries:
                """ start of the game, clicking the first country
                will place the first pathogen in the country """
                if country.contains_pt(pygame.mouse.get_pos()):
                    if infectionindex == 1:
                        country.infected_pop = country.infected_pop + 1
                        infectionindex = infectionindex - 1
                    country_pop_index = country
        """now our pathogen embarks on infection!"""

        """Upgrade functions that cost more and more as upgrades increase"""
        if event.type == pygame.KEYDOWN:
            #Upgrade infection rate
            if event.key == pygame.K_i:
                if Upgrade_Point > upgrades**2:
                    for country in countries:
                        country.infected_rate = country.infected_rate * 1.15
                    Upgrade_Point = Upgrade_Point - upgrades**2
                    upgrades = upgrades + 1
                    print (country.infected_rate)

            #increase kill rate
            if event.key == pygame.K_k:
                if Upgrade_Point > upgrades**2:
                    for country in countries:
                        country.death_rate = country.death_rate * 1.15
                    Upgrade_Point = Upgrade_Point - upgrades**2
                    upgrades = upgrades + 1
                    print (country.death_rate)
            #increase airborne capacity
            if event.key == pygame.K_a:
                if Upgrade_Point > upgrades**2:
                    for country in countries:
                        country.airborne_rate = country.airborne_rate + 0.15
                    Upgrade_Point = Upgrade_Point - upgrades**2
                    upgrades = upgrades + 1
                    print (country.airborne_rate)

    """Modify Time + XXXX to modify the speed of the game."""
    if pygame.time.get_ticks() > (Time + 1000):
        Time = pygame.time.get_ticks()
        if all(country.max_pop == 0 for country in countries) == True:
            running = False
            endscreen = True
        #print ('For each country: (infected ratio, total population)', (country1.infected_ratio(),country1.max_pop), (country2.infected_ratio(),country2.max_pop), (country3.infected_ratio(),country3.max_pop))
        Total_infected = 0

        """
        Infection types: step, death, propagation
        Upgrade Point is given at every step.
        """
        for country in countries:
            country.step()
            country.death()
            Total_infected += (country.infected_pop + country.dead_pop)
            if infectionindex == 0:
                if country.max_pop !=0:
                    if pygame.time.get_ticks() > (time + 2000):
                        time = pygame.time.get_ticks()
                        Upgrade_Point += random.randint(1,3)
            for other in countries:
                if country != other:
                    country.propagation(other)

        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # erases screen
    for country in countries:
        country.draw()

    """
    the number of infected, dead, and total population is displayed whenever we click certain country
    """
    screen.blit(font.render('Infected:%.2d'%(country_pop_index.infected_pop) + ' ' +'Dead:%.2d'%(country_pop_index.dead_pop) + ' '+ 'Alive:%.2d'%(country_pop_index.max_pop) +'        '+'Upgrade Point:%.2d'%(Upgrade_Point) , True, (0, 255, 255)), (0, 440))
    screen.blit(font.render('Current Upgrades:%.2d'%(upgrades), True, (0, 255, 255)), (400, 400))
    pygame.display.update()  # updates real screen from staged screen


while endscreen:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()


    text = basicfont.render('Congradulations you have killed everyone! Press Q to end the game.', True, (0, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)

    pygame.display.update()

pygame.quit()
