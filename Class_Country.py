"""
defining class country
Subeen Kim
"""

class country:

    def __init__(self, max_pop, infected_pop=0, infection_rate=1.1, center_x=100, center_y=200, radius=30):
        self.max_pop = max_pop
        self.infected_pop = infected_pop
        self.infection_rate = infection_rate
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def number_infection(self, click):
        """ click gets True of False from the mouse click """
        while click:
            self.infected_pop = self.infected_pop*self.infection_rate
            if self.infected_pop >= self.max_pop:
                break
            return int(self.infected_pop)

Egypt = country(1)
Egypt.max_pop = 100
number_infection(Egypt, True)
