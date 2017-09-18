# python-learning
# Code from Book Learn Python the Hardway
Summary of Topics and Code - Cheat Sheet

# Table of Contents
1. [Comments](#comments)
2. [Numbers Maths](#numbers_maths)
3. [Variables Names](#variables names)
4. [Strings and Text](#strings and text)
5. [Functions](#functions)


## Functions

def myFunction(entry_data):
    books = entry_data * 100
    tapes = books * 2
    bottles = tapes / 6
    return books, tapes, bottles
sum_num = 50

pens, paper, folders = myFunction(sum_num)
print "We have: pens %d, paper %d and folders %d" % (pens, paper, folders)
print "Or just one - number of pens %d" % pens
print "We have pens %d, paper %d and folders %d" % myFunction(entry_data)
   
