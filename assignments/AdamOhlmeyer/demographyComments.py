#!/usr/bin/env python

# Simulation to model demography on a landscape. This simulation 
# will include:
# - birth
# - death
# - dispersal

# First Version
# - Asexual reproduction
# - Annual generation times
# - Poisson-distributed number of offspring
# - Discrete landscape
# - Max dispersal of 1 grid
# - No diagonal dispersal
# - Equal probability of different directions
# - Non-zero probably of not dispersing
# - Starts in the middle
# - Start size of 50
# - No carrying capacity

# Object types
# - Individuals
# - Landscape
# - Cell

# Each generation first disperses, then reproduces

import numpy.random as nr 

# Class Definitions

#Defining class landscape 
class landscape:
   """This class holds all individuals across the landscape"""

#This is the constrictor, which details the objects being created in this class
   def __init__(self,nRows=5,nCols=5,startSize=50): #Starting init
       """
       Creates a new grid-based with the number of rows, columns, and 
       starting population size specified by the user.
       """
       self.nRows = nRows
       self.nCols = nCols
       self.startSize = startSize
       self.sections = self.setup(self.nRows,self.nCols)
       #for loop to append individuals
       for _ in range(self.startSize):
           self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))


# This sets up the grid orientation for the simulation
   def setup(self,nRows,nCols):
       """Sets up the landscape as a list of lists containing cells."""
       land = []
       for rowNum in range(nRows):
           row = []
           for colNum in range(nCols):
               row.append(cell(("%d_%d") % (rowNum,colNum))) #appends cell with row and column number
           land.append(row)
       return land

#This shows the landscape 
   def printLandscape(self):
       """Print all id numbers of cells in landscape"""
       #set up for loop to show number of individuals in each column and row
       for row in self.sections:
           for col in row:
               print("%d" % (len(col.individuals)), "\t", end="")
           print("\n") #prints number to screen

#Defining class cell
class cell:
   """This class represents a grid square on our landscape."""

#Defines the cell where all individuals start 
   def __init__(self,id):
       self.id = id
       self.individuals = []

#Defining class individual 
class ind:
   """This class represents individuals in our population."""

   #sets init for individuals and offspring in population 
   def __init__(self,myLandscape,myCell,name="",rowPos=0,colPos=0,disProb=0.5):
       self.myLandscape = myLandscape
       self.myCell = myCell
       self.name = name
       self.offspring = []
       self.meanOffNum = 2.0
       self.rowPos = rowPos
       self.colPos = colPos
       self.disProb = disProb

#Use poisson to set next generation offspring 
   def reproduce(self):
       """Return list of offspring"""
       numOff = nr.poisson(self.meanOffNum)
       offspringList = []
       #for loop to to set offspring range and append number of individuals after reproduction 
       for _ in range(numOff):
           offspringList.append(ind())
       return offspringList

#use to give the option of dispersing population by one cell or not moving 
   def disperse(self):
       """Move, if necessary, to new cell. disProb is dispersal probability."""

       if (nr.random() < self.disProb):

           # Middle cell
           if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
               ranNum = nr.random() #creating a random num variable
               #changing row position
               if (ranNum < 0.25):
                   self.rowPos = self.rowPos - 1
               elif (ranNum < 0.5):
                   self.rowPos = self.rowPos + 1
               #changing column position    
               elif (ranNum < 0.75):
                   self.colPos = self.colPos - 1
               else:
                   self.colPos = self.colPos + 1

           # Upper left cell
           elif (self.rowPos == 0) & (self.colPos == 0):
               ranNum = nr.random()
               if (ranNum < 0.5):
                   self.rowPos = self.rowPos + 1
               else:
                   self.colPos = self.colPos + 1

           # Left edge cell
           elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == 0):
               ranNum = nr.random()
               if (ranNum < 0.33):
                   self.rowPos = self.rowPos - 1
               elif (ranNum < 0.66):
                   self.rowPos = self.rowPos + 1
               else:
                   self.colPos = self.colPos + 1

           # Bottom left cell
           elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == 0):
               ranNum = nr.random()
               if (ranNum < 0.5):
                   self.rowPos = self.rowPos - 1
               else:
                   self.colPos = self.colPos + 1

           # Bottom edge cell
           elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
               ranNum = nr.random()
               if (ranNum < 0.33):
                   self.rowPos = self.rowPos - 1
               elif (ranNum < 0.66):
                   self.colPos = self.colPos - 1
               else:
                   self.colPos = self.colPos + 1

           # Bottom right cell
           elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
               ranNum = nr.random()
               if (ranNum < 0.5):
                   self.rowPos = self.rowPos - 1
               else:
                   self.colPos = self.colPos - 1

           # Right edge cell
           elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
               ranNum = nr.random()
               if (ranNum < 0.33):
                   self.rowPos = self.rowPos - 1
               elif (ranNum < 0.66):
                   self.rowPos = self.rowPos + 1
               else:
                   self.colPos = self.colPos - 1

           # Upper right cell
           elif (self.rowPos == 0) & (self.colPos == self.myLandscape.nCols-1):
               ranNum = nr.random()
               if (ranNum < 0.5):
                   self.rowPos = self.rowPos + 1
               else:
                   self.colPos = self.colPos - 1

           # Upper edge cell
           else:
               ranNum = nr.random()
               if (ranNum < 0.33):
                   self.rowPos = self.rowPos + 1
               elif (ranNum < 0.66):
                   self.colPos = self.colPos - 1
               else:
                   self.colPos = self.colPos + 1

#To kill previous population, so only offspring survive
           self.myCell.individuals.remove(self)
           self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self) #adding new generation from offspring
           self.myCell = self.myLandscape.sections[self.rowPos][self.colPos] #Add new generation to cell based on above if/else statement 

# Run demographic simulation

simLandscape = landscape()
print("Generation 0:"); print()
simLandscape.printLandscape()

#set the number of generations
gens = 20

for g in range(gens): 
   allIndividuals = []
   for r in range(simLandscape.nRows):
       for c in range(simLandscape.nCols):
           allIndividuals.extend(simLandscape.sections[r][c].individuals)
           #list of lists (rows and columns) extend adds list to the end of a list 

   for i in allIndividuals:
       i.disperse() #This runs the disperse command which was defined in class individual with if/else statement.

   print("Generation %d:" % (g+1)); print() #prints generation number for each grid-based landscape

   simLandscape.printLandscape() #prints the grid-based landscape
   
# DB: These are good comments, although more detail could be provided.