class Parent(object):
    
    def altered(self):
         print "PARENT altered() only function in PARENT class"# class PARENT has-a function called altered and takes one para

class Child(Parent):

    def altered(self):
        print "CHILD, before PARENT altered()"
        super(Child, self).altered()
        print "CHILD, after PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
print " "
print "Calling son.altered()"
print " "
son.altered()
