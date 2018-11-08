#!/usr/bin/env python

# Simulation to model demography on a landscape. This simulation
# will include:
# - Birth
# - Death
# - Dispersal

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

# Set up for class landscape, defining variables, setting up rows and columns, and printing landscape.

class landscape:
    """This class holds all individuals across the landscape"""
# Defining a method to create a grid based with number or rows, columns, and starting population size.
    def __init__(self,nRows=5,nCols=5,startSize=50):
        """Creates a new grid-based with the number of rows, columns, and
	   starting population size specified by the user."""
        self.nRows = nRows
        self.nCols = nCols
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nCols)
        for _ in range(self.startSize):	# For loop to append individuals.
            self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))


    def setup(self,nRows,nCols):	# Set up for organization of grid.
        """Sets up the landscape as a list of lists containing cells."""
        land = []	# Creating an empty list for landscape.
        for rowNum in range(nRows):
            row = []
            for colNum in range(nCols):	# For loop that appends cell with row and column number.
                row.append(cell(("%d_%d") % (rowNum,colNum)))
            land.append(row)
        return land

    def printLandscape(self):
        """Print all id numbers of cells in landscape"""
        for row in self.sections:	# For loop that shows individuals in columns and rows.
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="")
            print("\n")

# Set up for class cell, which represents one area of the landscape.

class cell:
    """This class represents a grid square on our landscape."""
# Cell that all individuals start in.
    def __init__(self,id):
        self.id = id
        self.individuals = []

# Set up for class individual, defining variables, coming up with random number of offspring, and random disperal.

class ind:
    """This class represents individuals in our population."""

    def __init__(self,myLandscape,myCell,name="",rowPos=0,colPos=0,disProb=0.5):
        self.myLandscape = myLandscape
        self.myCell = myCell
        self.name = name
        self.offspring = []
        self.meanOffNum = 2.0
        self.rowPos = rowPos
        self.colPos = colPos
        self.disProb = disProb

    def reproduce(self):	# Useing poisson to generate random number of offspring per individual.
        """Return list of offspring"""
        numOff = nr.poisson(self.meanOffNum)
        offspringList = []
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList

    def disperse(self):	# Gives the option of dispersing population by one cell or not move at all.
        """Move, if necessary, to new cell. disProb is dispersal probability."""

# If/Elif statements for random dispersal and where dispersal will occcur.

        if (nr.random() < self.disProb):

            # Middle cell
            if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.25):
                    self.rowPos = self.rowPos - 1
                elif (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
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

            self.myCell.individuals.remove(self) # Kills off previoius generation to result in one generation at a time.
            self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self) # Adds new generation.
            self.myCell = self.myLandscape.sections[self.rowPos][self.colPos] # Adds new generation to cell based on above.

# Run demographic simulation

simLandscape = landscape()
print("Generation 0:"); print()
simLandscape.printLandscape()

# Initializes number of generations to run.
gens = 20

for g in range(gens):	# For loop that creates empty list for each generation.
    allIndividuals = []
    for r in range(simLandscape.nRows):
        for c in range(simLandscape.nCols): # For loop for each column adds individuals from landscape
            allIndividuals.extend(simLandscape.sections[r][c].individuals)

    for i in allIndividuals:	# Randomizes positions of every individual in the array allIndividuals
        i.disperse()
# Prints out grid dispersal in the landscape for every generation.
    print("Generation %d:" % (g+1)); print()

    simLandscape.printLandscape()
