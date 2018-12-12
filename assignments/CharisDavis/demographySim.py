#!/usr/bin/env python 

#Simulation to model demography on a landscape. This simulation will include:
#birth
#death
#dispersal 

#First Version
#- Asexual reproduction
#- Annual generation times
#- Poisson-distributed number of offspring
#- Discrete landscape
#- max dispersal of 1 grid
#- No diagonal dispersal
#- Equal probability of different directions
#- Non zero probability of not dispersing 
#- Starting population in the middle 
#- Starting pop size is 50
#- No carrying capacity

# Object Types
#- Individuals
#- Landscape 
#- Cell

import numpy.random as nr 
#now we can access the random library as nr

#Class Definitions
class landscape:
   """This class holds all individuals across the landscape"""
def __init__(self,nRows=5,nColumns=5, startSize=50):
        self.nRows = nRows
        self.nColumns = nColumns
        self.sections = self.setup(self.nRows,self.nColumns)
        for _ in range(startSize):
            self.sections[0][0].individuals.append(ind())
#rang function gives us a list of zero through 49
# the zero zero in the sublist it will show it in the upper lefthand corner
# cells should start at zero and increase by adding one cell each time
def setup(nRows,nColumns):
    """Sets up the landscape as a list of lists containing cells"""
cellID = 0
land  = []
for rowNum in range(nRows):
        row = []
for colNum in range(nColumns):
        row.append(cell(cellID))
        cellID = cellID + 1
        land.append(row)
        return land

def printLandscape(self):
    """Print all id numbers of cells in landscape"""
for row in self.sections:
        print ("New Row:")
        for col in row:
            print(col.id)
            print("Number of individuals: %d" % (len(col.individuals)))
#%d tells us its some integer value and on the right that represents how individuals are in each list in  each cell.the list of individuals 
#The loop to define number of times
		# return  list
# created this cell class to keep track of each cell
class cell:
   """This class represents a grid square on our landscape."""
def __init__(self,id,individuals=[]):
        self.id = id
        self.individuals = individuals

#creating an individual class
class ind:
   """This class respresents individuals in our popualtion."""
	#every class needs a constructor always beginning with self
def __init__(self,name=""):
        self.name = name
        self.offspring = []
        self.meanOffnum = 2.0
        self.colPos = colPos
#meanOffnum tells us the fecundity rate 
def reproduce(self):
    """Return list of offspring""" 
numOff = nr.poisson(self.meanOffNum)
offspringList = []
for _ in range(numOff):
        offspringList.append(ind())
        return offspringList

def disperse(self):
    """Move, if necessary """
#Actually do stuff
myLandscape = landscape()
myLandscape.printLandscape()

# DB: This is a good start, but most of the demography code seems to be missing. The comments are also a bit sparse.
