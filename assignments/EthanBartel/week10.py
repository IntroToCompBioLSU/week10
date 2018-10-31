#!/usr/bin/python

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
# Defining Class "Organism"
class organism:
    """Class to hold information about organisms I collect."""
    common = ""
    species = ""	#latin name
    color = ""
    popgrow = 0.0
    carrycap = 0
    startpop = 0
    numgen = 0
#defining Organism ind_1
ind_1 = organism()
ind_1.common = "Green_Tree_Frog"
ind_1.species = "Hyla_cinerea"
ind_1.color = "green"
ind_1.popgrow = 0.4
ind_1.carrycap = 1500
ind_1.startpop = 100
ind_1.numgen = 100

#defining organism 2
ind_2 = organism()
ind_2.common = "Nutria_Rat"
ind_2.species = "Myocastor_coypus"
ind_2.color = "Brown"
ind_2.popgrow = 0.7
ind_2.carrycap = 2500
ind_2.startpop = 100
ind_2.numgen = 100

#defining organism 3
ind_3 = organism()
ind_3.common = "Corn_Snake"
ind_3.species = "Pantherophis_guttatus"
ind_3.color = "Orange"
ind_3.popgrow = 0.6
ind_3.carrycap = 2000
ind_3.startpop = 100
ind_3.numgen = 100

#defining organism 4
ind_4 = organism()
ind_4.common = "Brown Pelican"
ind_4.species = "Pelecanus_occidentalis"
ind_4.color = "Brown"
ind_4.popgrow = 0.2
ind_4.carrycap = 5000
ind_4.startpop = 400
ind_4.numgen = 100

#Input and Formatting
#change ind_1 to other organisms to change the experiment

r = (ind_1.popgrow)
K = (ind_1.carrycap)
t = (ind_1.numgen)
p = (ind_1.startpop)
t = int(t)
K = int(K)
r = float(r)
p = int(p)
#setting start
num = [p]*(t+1)
#logistic growth model equation
for i in range(t): 
    num[i+1] = num[i]+r*num[i]*(1-num[i]/K)
#Plotting results
plt.plot(range(t+1),num, 'b')
plt.xlabel('Generation')
plt.ylabel('Number')
plt.title('Growth rate: %s, Carrying Capacity = %d' % (r, K))
plt.axvline(np.argmax(np.diff(num)),  color = 'k' )
plt.show()