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
Defining a Function
You can define functions to provide the required functionality. Here are simple rules to define a function in Python.
- Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
- Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
- The first statement of a function can be an optional statement - the documentation string of the function or docstring.
- The code block within every function starts with a colon (:) and is indented.

The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

# Syntax
```
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
   ```
By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.
https://www.tutorialspoint.com/python/python_functions.htm
