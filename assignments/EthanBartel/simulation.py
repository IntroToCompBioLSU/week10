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
#defining Class Landscape
class landscape:
    """This class holds all individuals across the landscape"""

    def __init__(self,nRows=5,nCols=5,startSize=50): #starting init
        """
        Creates a new grid-based with the number of rows, columns, and 
        starting population size specified by the user.
        """
        #Creating Grid
        self.nRows = nRows
        self.nCols = nCols
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nCols)
        for _ in range(self.startSize):
            self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))
#for Loop to append individual 

    def setup(self,nRows,nCols):
        """Sets up the landscape as a list of lists containing cells."""
        land = [] #creating land list
        for rowNum in range(nRows):
            row = []
            for colNum in range(nCols):
                row.append(cell(("%d_%d") % (rowNum,colNum))) #for loop appends cell row and column info to row
            land.append(row) #appends row to land
        return land

    def printLandscape(self):
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="") #for loop printing grid
            print("\n")
#defining Class Cell
class cell:
    """This class represents a grid square on our landscape."""

    def __init__(self,id):
        self.id = id
        self.individuals = []
#defining Class individual
class ind:
    """This class represents individuals in our population."""
    
    def __init__(self,myLandscape,myCell,name="",rowPos=0,colPos=0,disProb=0.1):
        self.myLandscape = myLandscape
        self.myCell = myCell
        self.name = name
        self.offspring = []
        self.meanOffNum = 2.0
        self.rowPos = rowPos
        self.colPos = colPos
        self.disProb = disProb

    def reproduce(self):
        """Return list of offspring"""
        numOff = nr.poisson(self.meanOffNum)
        offspringList = []
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList
#Defining the function disperse
#a lot of if else/elif statements
    def disperse(self):
        """Move, if necessary, to new cell. disProb is dispersal probability."""
        if (nr.random() < self.disProb): 

            # Middle cell 
            if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random() #creating ranNum variable
                if (ranNum < 0.25):
                    self.rowPos = self.rowPos - 1 #change row position based on chance by ranNum
                elif (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                elif (ranNum < 0.75):
                    self.colPos = self.colPos - 1 #change column position based on chance by ranNum
                else:
                    self.colPos = self.colPos + 1

            # Upper left cell
            elif (self.rowPos == 0 & self.colPos == 0):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1 #change row
                else:
                    self.colPos = self.colPos + 1 #change col

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
                if (ranNum < 0.5): #only .5 because of two options 
                    self.rowPos = self.rowPos - 1
                else:
                    self.colPos = self.colPos - 1

            # Right edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.33):#NOTE: only .33 instead of .25 because there are only 3 possible directions instead of 4
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos - 1

            # Upper right cell
            elif (self.rowPos == 0) & (self.colPos == self.myLandscape.nCols-1):#if the position meets both requirements
                ranNum = nr.random()
                if (ranNum < 0.5): #only .5 because of two options 
                    self.rowPos = self.rowPos + 1
                else:
                    self.colPos = self.colPos - 1

            # Upper edge cell 
            else:
                ranNum = nr.random()
                if (ranNum < 0.33): #NOTE: only .33 instead of .25 because there are only 3 possible directions instead of 4
                    self.rowPos = self.rowPos + 1
                elif (ranNum < 0.66):
                    self.colPos = self.colPos - 1
                else:
                    self.colPos = self.colPos + 1

            self.myCell.individuals.remove(self) #kill previous population
            self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self) # adding new generation 
            self.myCell = self.myLandscape.sections[self.rowPos][self.colPos] #adding new generation to their cell based on above 

# Run demographic simulation

simLandscape = landscape()
print("Generation 0:"); print()
simLandscape.printLandscape()
#sets generation number
#change this to increase or decrease the number of generations to run the simulation
#If you go over 20 there is a high chance of 
gens = 10

for g in range(gens):
    allIndividuals = [] #creating allIndividuals list
    for r in range(simLandscape.nRows): #for every row
        for c in range(simLandscape.nCols): #for every column 
            allIndividuals.extend(simLandscape.sections[r][c].individuals) #extend the individuals location to "All individuals"

    for i in allIndividuals: 
        i.disperse() #for loop to run the disperse that was defined above under class ind

    print("Generation %d:" % (g+1)); print() #print the number of generations 

    simLandscape.printLandscape() #Running print landscape