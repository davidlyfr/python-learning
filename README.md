# python-learning
# Code from Book Learn Python the Hardway
Summary of Topics and Code - Cheat Sheet

#### Table of Contents
[Comments](#comments)
[Working with Files](#working with files)
[Variables Names](#variables names)
[Strings and Text](#strings and text)
[Functions](#functions)

<a name="working with files"/>
## Working with Files

```
txt = open(filename) # file is opened and contents are a variable called txt
print txt.read() # print to screen

new_txt = open(filename, "ab") # append to a file
new_txt.write(add_to_file)    # add to the file the contents of variable 'add_to_file_
new_txt.write("\n")           # jump to a new line in the file
```

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
