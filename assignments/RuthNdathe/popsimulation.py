#!/usr/bin/env python

#import numpy library
import numpy.random as nr

#create class individual
class ind:
        """Class of individuals in our demographic simulation"""
        def __init__(self,lam=3,generations=1):
                self.lam=lam
                self.generations=generations
                self.numoffspring=nr.poisson(self.lam)
                newpop=[]
		
		#define method for  individuals to reproduce in different generations 
        def reproduce(self,generations=5):
                self.newpop=[]
                self.numoffspring= nr.poisson(self.lam)
                for gen in range(generations):
                        self.newpop.append(self.numoffspring)
                return self.newpop

#create class generation
class generation:
        def __init__(self,generation=10):
                self.generation=generation

#select parameters for several individuals and print the newpopulation in several generations
ind_2=ind(4)
ind_3=ind(3)
ind_4=ind(2)
print("New population")
for ind in (ind_2,ind_3,ind_4):
        print(ind.reproduce())


# DB: I think this is a really good start. I realize now that this was a lot to ask right after we just
#     started covering objects. Hopefully the later assignments helped.
