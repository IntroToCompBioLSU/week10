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
# Import numpy to run the array 
import numpy.random as nr 

# Class Definitions
# defining the landscape class (as an object?)
class landscape:
    """This class holds all individuals across the landscape"""

# the constructor along with the attributes of "landscape"
    def __init__(self,nRows=5,nCols=5,startSize=50):
        """
        Creates a new grid-based with the number of rows, columns, and 
        starting population size specified by the user.
        """
        self.nRows = nRows
        self.nCols = nCols
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nCols)
        # this for loop appends an individual in the landscape
        for _ in range(self.startSize):
            self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))


    def setup(self,nRows,nCols):
        """Sets up the landscape as a list of lists containing cells."""
        land = []
        for rowNum in range(nRows):
            row = []
            # appends a cell to a row/column value
            for colNum in range(nCols):
                row.append(cell(("%d_%d") % (rowNum,colNum)))
            land.append(row)
        return land

    def printLandscape(self):
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="")
            print("\n") # prints the grid to the screen when the program is run

# new class
class cell:
    """This class represents a grid square on our landscape."""

# constructor and attributes of "cell"
    def __init__(self,id):
        self.id = id
        self.individuals = []

# individuals class
class ind:
    """This class represents individuals in our population."""
    
    # constructor and attributes of an individual (where it is in the lanndscape)
    def __init__(self,myLandscape,myCell,name="",rowPos=0,colPos=0,disProb=0.5):
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
        numOff = nr.poisson(self.meanOffNum) # poisson dostribution for generating offspring 
        offspringList = []
        # for loop: sets the range for offspring and appends individuals 
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList

    def disperse(self):
        """Move, if necessary, to new cell. disProb is dispersal probability."""
        
        if (nr.random() < self.disProb):
# dispersal commands. The if/else statements are to set the parameters of their movement, which is one unit
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

            self.myCell.individuals.remove(self) # our form of population control, removes individuals each generation
            self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self) # new generation after removing the previous
            self.myCell = self.myLandscape.sections[self.rowPos][self.colPos] # 

# Run demographic simulation
# Do stuff
simLandscape = landscape()
print("Generation 0:"); print()
simLandscape.printLandscape()

# number of generations to run
gens = 20

# 
for g in range(gens):
    allIndividuals = []
    for r in range(simLandscape.nRows):
        for c in range(simLandscape.nCols):
            allIndividuals.extend(simLandscape.sections[r][c].individuals) # list extension of all individuals (list of a list)

# uses the dispersal object from above to disperse the individuals randomly
    for i in allIndividuals:
        i.disperse()

    print("Generation %d:" % (g+1)); print()
    # prints each landscape (grid system) for each generation (i.e, 20 times)

    simLandscape.printLandscape()

# DB: Your comments are good and get at the overall structure of the code, but it would be
#     helpful to have more detail. 

