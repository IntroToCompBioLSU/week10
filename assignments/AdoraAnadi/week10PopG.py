#!/usr/bin/env python

# (Attempted to) Refactor your population growth simulation to use objects that you define. 
# Include these object types:
#Individual
#Generation
#Simulation
#Each of these object types should have at least one property (variable) and one method
#Your Simulation class should have a run() method, so that you can run an entire simulation just by calling that method.

import numpy
import numpy.random as nr
import matplotlib.pyplot as plt

# Class of individuals 
class individual:
    """Class to hold information about individuals in population simulation."""

# Defining individuals (constructor)
    def __init__(self, gen=10, offspring=1): 
        self.gen = gen
        self.offspring = offspring

    def reproduce(self):
        self.offspring = nr.poisson(self.offspring)

#ind_1 = individual()
#ind_1.reproduce()
#ind_1.popgrowth =0.5
#ind_1.carrycap =1500
#ind_1.startpop =50
#ind_1.numgen =100

# Class of generations
class generation:
    """Class to hold information about generations of individuals."""
    
# Defining generation (constructor)
    def __init__(self, carrCap=1500, growth=individual.reproduce, startpop=50):
        self.carrCap = carrCap #carrying capacity
        self.growth = growth #growth rate
        self.startpop = startpop #starting population size

    def model(self):
        for i in range(generation):
            startpop[i+1] = startpop[i] + growth*startpop[i] * (1 - startpop[i]/carrCap)

# Class for simulation
class simulation:
    """Class to hold information about population simulation."""
    
# Defining simulation (constructor)
    def __init__(self, sim=generation.model):
        self.sim = sim

# Function to run simulation and plot
    def run(sim):
        plt.plot(range(generation+1), startpop, color='purple')
        plt.xlabel("Generations")
        plt.ylabel("Population")
        plt.title("Population Growth Simulation")
        txt=("Growth Rate: %s, Carrying Capacity: %d" % (r,K))
        plt.axvline(numpy.argmax(numpy.diff(num)), color = 'k' )
        plt.show()
        
# DB: I appreciate the attempt and the fact that you've defined the appropriate classes.
#     I don't think this will run as is, without some restructuring, but this was a lot 
#     to ask of you right after we started learning about classes.
