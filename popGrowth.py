#!/usr/bin/env python

import numpy.random as nr

class ind:
	"""Class for individuals in our demographic simulation. """

	def __init__(self,lam=3.0,gen=1,numOffspring=1):
		self.lam = lam
		self.gen = gen
		self.numOffspring = numOffspring

	def reproduce(self):
		self.numOffspring = nr.poisson(self.lam)
ind_1 = ind()
in_1.reproduce()
print(ind_1.numOffspring)


