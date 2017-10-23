"""
Victor Bianchi - SoftDes MP4 - Fall 2017 - Plague.BETA
This code is a basic structure to
the Virus class of the infamous game, Plague.
Figuring the different game mechanics and mathematics behind the virus
Has proven to be difficult.
RAw code does not compile and only represents the basic structure
the game should implement.
"""

class Virus():

    #Class constants and to reset game
    WORLD_POPULATION = 7 000 000 000
    INITIAL_INFECTION_RATE = 1.05
    HEALTHY_POPULATION = WORLD_POPULATION
    SICK_POULATION = 0
    DEAD_POPULATION = 0.99999 #To account for natural deaths

    #We should have an external CSX/XML file
    #to load the different countries
    #User should be able to choose between a country, a random country in
    #a continent or Random.
    countries_set = set(Canada, United States, Mexico)#and others
    first_infected;

def new_plague(self, first_inefected = None):
    """Creates new virus"""

    infection = INITIAL_INFECTION_RATE

    first_country = input('Choose starter country by entering country name or type Random')

    #with open (file, 'countries_list') as f:
        #for input in f:
    while input in countries_set or input == 'Random':
        if first_country in countries_set:
            return input
        else #first_country == 'Random':
            first_country = random.choice(countries)

    print('Please try again')
        new_plague()

    if first_infected is None:
        #start infection
        healthy = HEALTHY_POPULATION - 1
        sick = SICK_POPULATION + 1
    #start new round()

def new_round():
    """ THis function initiates the new round"""
    rounds = 0
    #9 different upgrade variables
    #Can be converted to a list later on
    t0 = 0;
    t1 = 0;
    t2 = 0;
    s3 = 0;
    s4 = 0;
    s5 = 0;
    a6 = 0;
    a7 = 0;
    a8 = 0;

    print('Would you like to increase transmission, symptoms, or the diseases abilities ?'')
    round_user_choice = input('Type T, S, A, or hit the space bar to skip')

    #Increase transmission = 0, 1, 2,
    if input == 'T':
        upgrade_choice == input("Would you like to increase airborne, rodent based, meat based tramission")
        if upgrade_chocie.islower() == 'airborne':
            return  t0++
        elif upgrade_choice.islower() == 'rodent':
            return t1++
        elif upgrade_choice.islower() == 'meat':
            return t2++
        #Increase Symptoms = 3, 4, 5
    elif input == 'S':
        if upgrade_chocie.islower() == 'insanity':
            return t3++
        elif upgrade_choice.islower() == 'necrosis':
            return t4++
        elif upgrade_choice.islower() == 'inflammation':
            return t5++
    #Increase abilities = 6, 7, 8
    elif input == 'A':
        if upgrade_chocie.islower() == 'drug':
                return t6++
        elif upgrade_choice.islower() == 'cold':
                return t7++
        elif upgrade_choice.islower() == 'hereditary':
                return t8++
    #Skip round
    elif input == ' ':

    else:#user error
        print('Try again')

    rounds += 1

def infection_upgrade(t0,t1,t2,s1,s2,s3,s4,s5,a6,a7,a8):
    #for every upgrade made to a variable, increase coefficient by x
    #Ex: 1.00 -> 1.05 -> 1.1

def infection_length():
    #This function will define how long it takes for someone to die after getting infected

def infect():
    #This function constantly infects people, can happen between each round
    #SICK_POPULATION * INFECTION_RATE


#4 Upgrades for 3 categories
#Transmission (airborne, rodent based, meat based)
#Symptoms(insanity, necrosis, inflammation )
#Abilities (drug resistance, cold resistance, hereditary )
#Increase infection rate
