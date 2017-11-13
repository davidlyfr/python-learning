## Animal is-a object (yes, sort of confusing) look at the extra credit
print ("\n" * 100)
class Animal(object):
    pass
## make a class named Animal that is-a object
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a init that takes self and name parameters
        self.name = name
        print name

## from self get the name value and set it to name
class Cat(Animal):

    def __init__(self, name):
        ## class has-a init that takes self and name paramters
        self.name = name
        # cat has-a name of some kind
        print name
## from self get the name value and set it to name
class Person(object):

    def __init__(self, name):
        ## class Person has-a init that takes self and name parameters
        self.name = name
        ## person has-a pet of some kind
        self.pet = None

class Employee(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
        print name, number
## class employee has-a init that takes self, name and number parameters
## employee has-a name of some kind
## employee has-a number of some kind
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

class Fleetmatics(object):
    def __init__(self, name):
        self.name = name
        print "%s works at Fleetmatics" % name

class awsugn(myvalue):
    def __init__(self, name):
        self.name = name
        print name

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ?? 
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

##??
crouse = Salmon()

## ??
harry = Halibut()
david = Fleetmatics("David")

####################################
dog = Animal()
POC = awsugn("DT")
