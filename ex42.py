## Animal is-a object (yes, sort of confusing) look at the ectra credit
class Animal(object):
    pass
## ??
class Dog(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name
        print name

## ??
class Cat(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name
        print name
## ??
class Person(object):
  
    def __init__(self, name):
        ## ??
        self.name = name
        ## person has-a pet of some kind
        self.pet = None

class Employee(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
        print name, number
## ??    
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
