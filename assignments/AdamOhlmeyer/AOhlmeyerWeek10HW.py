#!/usr/bin/env python


#- [ ] Refactor your population growth simulation to use objects that you define.
# Include these object types:
 #  Individual
  #- Generation
  # Simulation
  # Each of these object types should have at least one property (variable) and one method
  # Your Simulation class should have a `run()` method, so that you can run an entire simulation just by calling that method.


# t(number of generations) and K(carrying capacity) must be whole numbers
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

#set organism as object
class organism: 
	"""defining organism"""
	popgrowth = 0.0
	carrycap = 0
	startpop = 0
	numgen = 0
#defining organism

ind_1 = organism()
ind_1.popgrowth =0.5
ind_1.carrycap =1500
ind_1.startpop =50
ind_1.numgen =100

#set imput for population formula with starting population, generations and max capacity. 
r = (ind_1.popgrowth)
K = (ind_1.carrycap)
t = (ind_1.numgen)
p = (ind_1.startpop)
t = int(t)
K = int(K)
r = float(r)
p = int(p)
#set starting number and popultion
num = [p]*(t+1)
#log. growth population equation model 
for i in range(t): 
    num[i+1] = num[i]+r*num[i]*(1-num[i]/K)
# graphing results with plot
plt.plot(range(t+1),num, 'b')
plt.xlabel('Generation')
plt.ylabel('Number')
plt.title('Growth rate: %s, Carrying Capacity = %d' % (r, K))
plt.axvline(np.argmax(np.diff(num)),  color = 'k' )
plt.show() 
