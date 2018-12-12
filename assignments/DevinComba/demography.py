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

class landscape:
    """This class holds all individuals across the landscape"""

    def __init__(self,nRows=5,nCols=5,startSize=50):
        """
        Creates a new grid-based with the number of rows, columns, and 
        starting population size specified by the user.
        """
        self.nRows = nRows
        self.nCols = nCols
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nCols)
        for _ in range(self.startSize):
            self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))


    def setup(self,nRows,nCols):
        """Sets up the landscape as a list of lists containing cells."""
        land = []
        for rowNum in range(nRows):
            row = []
            for colNum in range(nCols):
                row.append(cell(("%d_%d") % (rowNum,colNum)))
            land.append(row)
        return land

    def printLandscape(self):
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="")
            print("\n")

class cell:
    """This class represents a grid square on our landscape."""

    def __init__(self,id):
        self.id = id
        self.individuals = []

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

    def reproduce(self):
        """Return list of offspring"""
        numOff = nr.poisson(self.meanOffNum)
        offspringList = []
        for _ in range(numOff):
            offspringList.append(ind())
        return offspringList

    # Given the dispersal probability, this individual will either disperse or stay put.
    def disperse(self):
        """Move, if necessary, to new cell. disProb is dispersal probability."""
        
        # Based on dispersal probability, randomly disperses.
        if (nr.random() < self.disProb):

            # Depending on the dispersal directions available, choose one at random and move in that direction.
            
            # Middle cell
            # If the individual is not in the first or last row and not in the first or last column.
            if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
                # Random number between 0 and .25, move up one cell
                if (ranNum < 0.25):
                    self.rowPos = self.rowPos - 1
                # Random number between.25 and .50, move down one cell
                elif (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                # Random number between .50 and .75, move left one cell
                elif (ranNum < 0.75):
                    self.colPos = self.colPos - 1
                # Random number between .75 and 1, move right one cell
                else:
                    self.colPos = self.colPos + 1

            # Upper left cell
            # If the individual is in the first row and first column
            elif (self.rowPos == 0) & (self.colPos == 0):
                ranNum = nr.random()
                # Move right one cell.
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1
                # Move down one cell
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

            self.myCell.individuals.remove(self)
            self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self)
            self.myCell = self.myLandscape.sections[self.rowPos][self.colPos]

# Run demographic simulation

simLandscape = landscape()
print("Generation 0:"); print()
simLandscape.printLandscape()

gens = 20

for g in range(gens):
    allIndividuals = []
    for r in range(simLandscape.nRows):
        for c in range(simLandscape.nCols):
            allIndividuals.extend(simLandscape.sections[r][c].individuals)

    for i in allIndividuals:
        i.disperse()

    print("Generation %d:" % (g+1)); print()

    simLandscape.printLandscape()
    
# DB: The comments are good, although a bit sparse. I was hoping for a bit more throughout,
#     although I know this is a lot of code to get through.