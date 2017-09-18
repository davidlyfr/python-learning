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

```
def myFunction(entry_data):
    pens = entry_data * 100
    paper = pens * 2
    bottles = paper / 6
    return pens, paper, bottles
sum_num = 50

pens, paper, bottles = myFunction(sum_num)
print "We have: pens %d, paper %d and bottles %d" % (pens, paper, bottles)
print "Or just one - number of pens %d" % pens
print "We have pens %d, paper %d and folders %d" % myFunction(entry_data)
```
