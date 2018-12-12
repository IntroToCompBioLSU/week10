#!/usr/bin/env python


 # Different object types:
 # Individual
 # Generation
 # Simulation
 # Each object type should have a minimum of one property (variable) and one method
 # Simulation class contains`run()` method to allow you to run an entire simulation just by calling that method.


# t(number of generations) and K(carrying capacity) can only be used as whole numbers
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

#createthe the term organism as an object
class organism: 
	"""define the organism"""
	popg = 0.0
	ccap = 0
	startp = 0
	numgeneration = 0
#Now define the term organism

ind_1 = organism()
ind_1.popg =1
ind_1.ccap =1000
ind_1.startp =100
ind_1.numgeneration = 25

#set input for population formula with these: starting population, generations and max capacity. 
f = (ind_1.popg)
K = (ind_1.ccap)
t = (ind_1.numgeneration)
p = (ind_1.startp)
t = int(t)
K = int(K)
f = float(f)
p = int(p)
#Go ahead and set starting number and population
num = [p]*(t+1)
#log. growth pop equation model 
for i in range(t): 
    num[i+1] = num[i]+f*num[i]*(1-num[i]/K)
# graphing results with plot
plt.plot(range(t+1),num, 'b')
plt.xlabel('Generation')
plt.ylabel('Number')
plt.title('Growth rate: %s, Carrying Capacity = %d' % (f, K))
plt.axvline(np.argmax(np.diff(num)),  color = 'k' )
plt.show() 

# DB: Not quite as extensive as I had originally laid out, but it's a nice use of a novel
#     class and it runs well.