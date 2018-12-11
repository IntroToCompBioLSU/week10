#!/usr/bin/env python

import numpy
import numpy.random as nr
import matplotlib.pyplot as plt

# setting up individuals class & reproduction function 
class ind:
    """Class for individuals in our demographic simulation."""

    def __init__(self, lam=3.0, gen=10, numOffspring=1):
        self.lam = lam
        self.gen = gen
        self.numOffspring = numOffspring

    def reproduce(self):
        self.numOffspring = nr.poisson(self.lam)

ind_1 = ind()
ind_1.reproduce()

# setting up generation class & growth rate/carrying capacity function
class gen:
    """Class for generations in our demographic simulation."""
    def __init__(self, cCap=500, gRate=ind.reproduce, p=10):
        self.cCap = cCap     ##carrying capacity
        self.gRate = gRate   ##growth rate
        self.p = p           ##number of individuals in starting population

    def model(self):
        for i in range(gen):
            p[i+1] = p[i] + gRate*p[i] * (1 - p[i]/cCap)

class sim:
    """Class for running simulation with pyplot."""
    def __init__(self, simulation=gen.model):
        self.simulation = simulation     ##function set up in generation class to model population growth + carrying capacity
## plot results of population simulation using pyplot
    def run(simulation):
        plt.plot(range(gen+1), p, color='purple')
## labeling axes & formatting
        plt.xlabel("Generations")
        plt.ylabel("Population Size")
        plt.title("Change in Population Size Over Generations")
        txt=("Growth Rate: %s, Carrying Capacity: %d" % (r,K))
        plt.figtext(0.5, 0.005, txt, wrap=True, horizontalalignment='center', fontsize=8, color='purple')
        plt.axvline(numpy.argmax(numpy.diff(num)), color = 'k' )
        plt.show()

### kept getting error saying run was not defined when I tried to use a 'run()' arguement

