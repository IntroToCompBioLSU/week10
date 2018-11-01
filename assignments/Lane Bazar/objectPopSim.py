#!/usr/bin/env python

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

#Refractor youpopulation grwoth simultion using objects such as individual, generation, and simulation, each with at least one variable. Run method should be present for the simulation.

#setting object, organism.

class organism:
	"""Organism Informaton"""
	popGrowth = 0.0
	carCapacity = 0
	startingPop = 0
	genNum = 0
#define organism ind_1
ind_1 = organism()
ind_1.popGrowth = 0.6
ind_1.carCapacity = 1000
ind_1.startingPop = 25
ind_1.genNum = 100

#establish a system for population to predict offspring per individual at rando$

p = nr.poisson()

#establish a variable for initial population size.
#currentPop = input("Type the starting population of indiviuduals: ")
currentPopulation = int(input("Initial population size: "))
cP = int(currentPopulation)
cP = (ind_1.startingPop)

#establish variable for carrying capacity
#maxPop = input("Type the carrying capacity of the enviroment: ")
carryingCapacity = int(input("Population carrying capacity: "))
cC = int(carryingCapacity)
cC = (ind_1.carCapacity)

#establish a variable for number of generation for growth
#genCount = input("Type the number of generations to be Simulated: ")
generationCount = int(input("Number of generations: "))
gC = int(generationCount)
gC = (ind_1.genNum)

p = float(p)
p = (ind_1.popGrowth)

#est. currentPop as the  initial population which is to have offSpring for cert$
pop = [cP]*(gC+1)

# loop generation count times
for i in range(gC):
        pop[i+1] = pop[i]+p*pop[i]*(1-pop[i]/cC)

#create a plot of my population growth through time.
plt.plot(range(gC+1),pop, 'b')
plt.xlabel('generation')
plt.ylabel('population')
plt.title('rate of growth: %s, carrying capacity = %d' % (p, cC))
plt.axvline(np.argmax(np.diff(pop)), color = 'k' )
plt.show()
