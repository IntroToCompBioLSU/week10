#!/usr/bin/env python

import numpy
import numpy.random as nr
import matplotlib.pyplot as plt

# Set up for class Individual.
class ind:
    """This class is for individuals in the population and reproduction of a randomly assigned offspring."""

    def __init__(self, lamd=4.0, gen=100, OffSpring=2):
        self.lamd = lamd
        self.gen = gen
        self.OffSpring = OffSpring

    def reproduce(self):
        self.OffSpring = nr.poisson(self.lamd)

ind_1 = ind()
ind_1.reproduce()

# Set up for class Generation adding parameters for carrying capacity, growth rate, and starting population number.

class gen:
    """This class is for generations of the population."""
    def __init__(self, K=350, growRate=ind.reproduce, p=30):
        self.K = K     # Carrying capacity of the population
        self.growRate = growRate   # Growth rate
        self.p = p           # Starting population size

    def model(self):
        for i in range(gen):
            p[i+1] = p[i] + growRate*p[i] * (1 - p[i]/K)

# Set up for class Simulation.

class sim:
    """This class is for simulating the population growth using pyplot."""
    def __init__(self, simulation=gen.model):
        self.simulation = simulation     # Function to model population growth + carrying capacity

# Plot results of population simulation.

    def run(simulation):
        plt.plot(range(gen+1), p, color='blue')

# Labels on axes & formatting of graph.

        plt.xlabel("Generations")
        plt.ylabel("Population Size")
        plt.title("Change in Population Size Over Generations")
        txt=("Growth Rate: %s, Carrying Capacity: %d" % (OffSpeing, K))
        plt.figtext(0.5, 0.005, txt, wrap=True, horizontalalignment='center', fontsize=8, color='blue')
        plt.axvline(numpy.argmax(numpy.diff(num)), color = 'k' )
        plt.show()
run()
