#!/usr/bin/env python

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
#
#class ind:
# """class for individuals in our population"""
#
#   def __init__(self,lam=3.0,generation=1,numOffspring=1):
#        self.lam = lam
#       self.gen = generation
#        self.numOffspring = numOffspring
#  def reproduce(self):
#        self.numOffspring = nr.poisson(self.lam)
#
#class generation:
#  """Total number of generations in the sim"""
#    def __init__(self,):
#
#   ind_1=ind()
#        ind_1.reproduce
#        print(ind_1.numOffspring)
#
# creating the object itself? 
# Still a little confused about the concept but hopefully the next assignment helps out as far as understanding its application
class org: 
    """Defining the organism (or individual)"""
    populationGrowth = 0.0
    carryingCapacity = 0
    initialPopulation = 0
    numofGenerations = 0

# defining the actual organism and its perameters
ind_1 = org()
ind_1.populationGrowth = 1.0
ind_1.carryingCapacity = 500
ind_1.initialPopulation = 10
ind_1.numofGenerations = 100

# population formula variables
r = (ind_1.populationGrowth)
K = (ind_1.carryingCapacity)
t = (ind_1.numofGenerations)
p = (ind_1.initialPopulation)
r = float(r)
K = int(K)
t = int(t)
p = int(p)
# formula to generate starting number
num = [p]*(t+1)
for x in range(t):
    num[x+1] = num[x]+r*num[x]*(1-num[x]/K)
# matplot executions
plt.plot(range(t+1),num, 'b')
plt.xlabel('Generations')
plt.ylabel('Growth (individuals)')
plt.title("Growth rate of a population")
plt.axvline(np.argmax(np.diff(num)), color = 'k' )
plt.show()