#!/usr/bin/env python


import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

#object
class organism:
	"""Setting Object"""
	popgrowth = 0.0
	carrycap = 0
	startpop = 0
	numgen = 0


ind_1 = organism()
ind_1.PopRate =0.25
ind_1.MaxPop =500000
ind_1.StartPop =50
ind_1.Gens =100

#Setting population
PopRate = (ind_1.PopRate)
MaxPop = (ind_1.MaxPop)
Gens = (ind_1.Gens)
StartPop = (ind_1.StartPop)
Gens = int(Gens)
MaxPop = int(MaxPop)
PopRate = float(PopRate)
StartPop = int(StartPop)
#Starting Population
num = [StartPop+1]*(Gens+1)
#Formula para iniciar el creciminto 
for i in range(Gens): 
    num[i+1] = num[i]+PopRate*num[i]*(1-num[i]/MaxPop)
# Graph
plt.plot(range(Gens+1),num,)
plt.xlabel('Generation')
plt.ylabel('Number')
plt.title('Growth rate: %s, Carrying Capacity = %d' % (PopRate, MaxPop))
plt.axvline(np.argmax(np.diff(num)),  color = 'g' )
plt.show()

# DB: I didn't see this file in a pull request, but found it on your fork of week 10.

# DB: Not quite as extensive as I had originally laid out, but it's a nice use of a novel
#     class and it runs well.