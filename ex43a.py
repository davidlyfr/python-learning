#!/usr/bin/python
# -*- coding: utf-8 -*-

#__init__
# self
# methods vs functions

class Human():
    
    def __init__(self, name, gender):

        self.name = name
        self.gender = gender

will = Human("William", "Male")
may = Human("Mary", "Female")

print will.name
print will.gender
print "\n"
print may.name
print may.gender
print "\n"

