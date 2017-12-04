class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"
  
    def altered(self):
        print "PARENT altered()"

    def my_print(self):
        print "Normal Print ---- %s " % (self)

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print " "
test = Parent()
test.my_print()
print " "
dad.override()
son.override()
print " "
dad.altered()
son.altered()
