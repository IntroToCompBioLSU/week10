# Week 10 Outline

## Final Project Ideas

- Some general ideas for final projects now posted on GitHub

## Reading

- Practical Computing, Chapters 10 and 11


## Running Population Growth Simulations

- Let's run some simulations using different code and starting conditions
- What happens when we run different code with the same starting conditions? Why?

## Objects in Python

- [ ] What is an object
  - We've already been using objects in Python whenever we create a variable
  - However, sometimes you need specific functionality that is hard to achieve using just the standard types.
  - Python, and any other object-oriented programming language, allows you to create your own types of objects that have whatever data and methods you'd like bundle together.
  - When talking about objects, we need to distinguish object classes from object instances. Think of classes as the generic categories (e.g., person) and instances as individuals in those categories (e.g., Drew Brees).
  - The nature of your classes depends entirely on the goals of your code. Think about the natural units with which you'd like to work.


- [ ] Defining your own Objects
  - Let's say we're doing a study where we collect different organisms and want to store information about them.
        class organism:
            """Class to hold information about organisms I collect."""
            id = ""
            species = ""      # Latin name
            latitude = 0.0
            longitude = 0.0
            length = 0.0      # units are mm
            color = ""
  - Now we can create instances of our organism for each individual we collect
        ind_1 = organism()
        ind_1    # What do you see when you examine ind_1 here?
        ind_1.id = "LSUMNS 45884"
        ind_1.species    # What about this?
        ind_1.species = "Hyla_cinerea"
        ind_1.latitude = 30.418419
        ind_1.longitude = -91.161132
        ind_1.length = 40
        ind_1.color = "green"
  - This is all well and good - we can create a new instanc of a custom object and define its properties - but it's somewhat cumbersome to set all the properties and we don't have a convenient way to summarize or otherwise intelligently use this information.
  - In addition to custom variables associated with object instances, we can also define custom methods. For instance, we could add this method to our class definition:
        def printLatLon(self):
            print("(%f,%f)" % (self.latitude,self.longitude))
  - Note that the `self` variable is a special reference to that instance of the object. So, to reference a variable that is part of the object from inside one of its methods, you'll need to start that variable reference with `self.<VARIABLE>`. `self` should be the first argument to all class methods.


- [ ] What is a constructor
  - As we defined the class above, the variables are technically owned by the class itself, and not individual instances of that class. This can lead to unexpected behavior. For instace, try this:
        class org:
            orgList = []
        ind_1 = org()
        ind_1.orgList.append(1)
        ind_2 = org()
        ind_2.orgList
        ind_2.orgList.append(2)
        ind_1.orgList
        # What's going on here?
  - To set variables for each instance of an object in an organized way, objects have a special method known as a constructor.
  - The purpose of the constructor is to provide a cohesive way to create new instances of a given class and set all variables appropriately.
  - The constructor always has a specific name with a special meaning: `__init__`.
  - Usually, if you want to define the values of variables for that instance, they are passed as arguments to the constructor. So, to define a constructor for our organism class, we could do the following:
        class organism():
            """Class to hold information about organisms I collect."""

            def __init__(self,id,sp,lat,lon,length,col):
                self.id = id
                self.species = sp
                self.latitude = lat
                self.longitude = lon
                self.length = length
                self.color = col
  - Now, to create `ind_1` with the same properties as above, we could do this:
        # I'm passing each argument on its own line, to make it easy to read
        ind_1 = organism("LSUMNS 45884",
                         "Hyla_cinerea",
                         30.418419,
                         -91.161132,
                         40,
                         "green")
  - You can also create default values for all the variables, which are included in the list of arguments to the constructor
        def __init__(self,id="1",sp="genus_species",lat=0.0,lon=0.0,length=0.0,col"black"):
            self.id = id
            self.species = sp
            self.latitude = lat
            self.longitude = lon
            self.length = length
            self.color = col
  - You can then create new individuals without passing any arguments to the constructor and the variables will take the default values:
        ind_1 = organism()
        ind_1.id
  - You can also pass just those variables you want to define, with the others taking default values:
        ind_1 = organism(color="green")
        ind_1.id
        ind_1.color


- [ ] Accessing and modifying object properties
 - The variables and methods of an instance can be accessed using the dot operator `<INSTANCE>.<VARIABLE>` or `<INSTANCE>.<METHOD>`.
 - To keep things organized, many programmers prefer to access or set variables using "getter" and "setter" methods:
        def setID(self,newID):
            self.id = newID
        def getID(self):
            return self.id


- [ ] Working with objects
 - Now that we've defined our custom class, we can work with instances of this class (objects) just like we would any other variable.
 - For instance, we can create a list of organisms:
        myOrganisms = []
        myOrganisms.append(organism(id="45",sp="Anolis_carolinensis"))
        myOrganisms.append(organism(id="23",sp="Hemidactylus_turcicus",col="grey"))
        myOrganisms
        for org in myOrganisms:
            print(org.id)
            print(org.color)


- [ ] Ok, those are all the basic principles for defining new classes, as well as creating instances with their associated variables and methods. Now it's just a matter of practice!

## Weekly Assignment

- [ ] Pick a general topic for your final project and find other team members

- [ ] Refactor your population growth simulation to use objects that you define. Include these object types:
  - Individual
  - Generation
  - Simulation
  - Each of these object types should have at least one property (variable) and one method
  - Your Simulation class should have a `run()` method, so that you can run an entire simulation just by calling that method.


## References
- [Python Class Documentation](https://docs.python.org/3/tutorial/classes.html)
