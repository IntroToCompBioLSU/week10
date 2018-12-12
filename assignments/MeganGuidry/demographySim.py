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
## Import numpy to use poisson in the reproduction method 
import numpy.random as nr 

# Class Definitions

class landscape:
    """This class holds all individuals across the landscape"""

    def __init__(self,nRows=5,nCols=5,startSize=50):		##landscape class contructor
        """
        Creates a new grid-based with the number of rows, columns, and 
        starting population size specified by the user.
        """
        self.nRows = nRows
        self.nCols = nCols
        self.startSize = startSize
        self.sections = self.setup(self.nRows,self.nCols)
        for _ in range(self.startSize):				##to loop through a list w/o value use underscore as variable name
            self.sections[0][0].individuals.append(ind(myLandscape=self,myCell=self.sections[0][0]))
				## double indexes to find the section(much like x,y coordinates)
				## add number of indviduals to the cell in the landscape


    def setup(self,nRows,nCols):				##setup method to create cells to store individuals
        """Sets up the landscape as a list of lists containing cells."""
        land = []		## start landscape list
        for rowNum in range(nRows):
            row = []		##row is a list within the land list
            for colNum in range(nCols):
                row.append(cell(("%d_%d") % (rowNum,colNum))) ##columns are created with cells 
            land.append(row)
        return land		##returns the the landscape with rows and columns to the command line

    def printLandscape(self):					##printLandscape method to print cell ID numbers
        """Print all id numbers of cells in landscape"""
        for row in self.sections:
            for col in row:
                print("%d" % (len(col.individuals)), "\t", end="")	##prints the number of individuals in a column
            print("\n")

class cell:
    """This class represents a grid square on our landscape."""

    def __init__(self,id):					##constructor for cell class
        self.id = id
        self.individuals = []

class ind:
    """This class represents individuals in our population."""
    
    def __init__(self,myLandscape,myCell,name="",rowPos=0,colPos=0,disProb=0.5):	##contructor for ind attributes
        self.myLandscape = myLandscape
        self.myCell = myCell
        self.name = name
        self.offspring = []
        self.meanOffNum = 2.0
        self.rowPos = rowPos
        self.colPos = colPos
        self.disProb = disProb

    def reproduce(self):				##defining reproduce function
        """Return list of offspring"""
        numOff = nr.poisson(self.meanOffNum)		##number of offspring is determined by a random number set with a poisson of 2
        offspringList = []				##created offspring list
        for _ in range(numOff):
            offspringList.append(ind())			##adding new offspring to list of offspring
        return offspringList

    def disperse(self):					##dispersal function
        """Move, if necessary, to new cell. disProb is dispersal probability."""
        
        if (nr.random() < self.disProb):		## if random number is less than probablity of dispersal do following things

            # Middle cell
            if (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()			## if you are in the middle cell...
                if (ranNum < 0.25):
                    self.rowPos = self.rowPos - 1	## and random number is less than 0.25, move down one cell;
                elif (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1	## if random number is less than 0.5, move up one cell;
                elif (ranNum < 0.75):
                    self.colPos = self.colPos - 1	## if random number is less than 0.75, move left one cell;
                else:
                    self.colPos = self.colPos + 1	## if random number anything else, move right one cell
							## the probability decimal for determining dispersal is based on number of 
							## movement options (i.e. if you have 4 different ways you can move, the 
							## ranges for probability will be split into quarters as seen above)
            # Upper left cell
            elif (self.rowPos == 0) & (self.colPos == 0):	## if you are in the upper left cell and...
                ranNum = nr.random()				
                if (ranNum < 0.5):				
                    self.rowPos = self.rowPos + 1		## random number is less than 0.5, move up one cell
                else:
                    self.colPos = self.colPos + 1		## if random number is greater than 0.5, move right one cell 

            # Left edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == 0): 
								## if you are in the left edge cell and...
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1		## random number is less than 0.33, move down one cell
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1		## if ... move up one cell
                else:
                    self.colPos = self.colPos + 1		## if ... move right one cell

            # Bottom left cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == 0):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos - 1		## if ... move down one cell
                else:
                    self.colPos = self.colPos + 1		## if ... move right one cell
            
            # Bottom edge cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos > 0) & (self.colPos < self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1		## move down one cell
                elif (ranNum < 0.66):
                    self.colPos = self.colPos - 1		## move left one cell
                else:
                    self.colPos = self.colPos + 1		## move right one cell

            # Bottom right cell
            elif (self.rowPos == self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos - 1		## move down one cell
                else:
                    self.colPos = self.colPos - 1		## move left one cell

            # Right edge cell
            elif (self.rowPos > 0) & (self.rowPos < self.myLandscape.nRows-1) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos - 1		## move down one cell
                elif (ranNum < 0.66):
                    self.rowPos = self.rowPos + 1		## move up one cell
                else:
                    self.colPos = self.colPos - 1		## move left one cell

            # Upper right cell
            elif (self.rowPos == 0) & (self.colPos == self.myLandscape.nCols-1):
                ranNum = nr.random()
                if (ranNum < 0.5):
                    self.rowPos = self.rowPos + 1		## up one 
                else:
                    self.colPos = self.colPos - 1		## left one

            # Upper edge cell
            else:
                ranNum = nr.random()
                if (ranNum < 0.33):
                    self.rowPos = self.rowPos + 1		## up one
                elif (ranNum < 0.66):
                    self.colPos = self.colPos - 1		## left one
                else:
                    self.colPos = self.colPos + 1		## right one

            self.myCell.individuals.remove(self)		## moves individuals from original cell
            self.myLandscape.sections[self.rowPos][self.colPos].individuals.append(self)
            self.myCell = self.myLandscape.sections[self.rowPos][self.colPos]

# Run demographic simulation

simLandscape = landscape()		## sets landscape
print("Generation 0:"); print()		
simLandscape.printLandscape()

gens = 20	## set number of generations

for g in range(gens):
    allIndividuals = []						## creates list for matrix of cells
    for r in range(simLandscape.nRows):
        for c in range(simLandscape.nCols):
            allIndividuals.extend(simLandscape.sections[r][c].individuals)

    for i in allIndividuals:
        i.disperse()			## runs the disperse function 

    print("Generation %d:" % (g+1)); print()

    simLandscape.printLandscape()	## prints out visualization of the lanscape


# DB: Nicely done. The comments are both helpful and numerous. A few of the more complicated sections lack comments,
#     but they're also not necessarily easy to understand.
