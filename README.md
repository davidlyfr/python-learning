# python-learning
# Code from Book Learn Python the Hardway
Summary of Topics and Code - Cheat Sheet

#### Table of Contents
1. [Comments-User Info](#comments)
2. [Starting Parameters](#python-start)
2. [Working with Files](#working-with-files)
3. [Variables Names](#variables-names)
4. [Strings and Text](#strings-and-text)
5. [Functions](#functions)
6. [Inputs](#inputs)
7. [Loops - For](#for_loops)
8. [String Formatting](#String-Formatting)
9. [Color](#color)

<a name="comments"></a>
# Comments - User Info

Check on arguments provided by user
```
from sys import argv
import sys

if len(sys.argv) != 2:
    print "\nUsage: target-ip file or single ip <file name> "
    print "\tInfo: For now it can receive one ip"
    print "\tInfo: IPv4 only"
    sys.exit(0)
```    
Or just give them info anyway:
```
def usage():
    print "BHP Net Tool"
    print
    print "Usage: bhpnet.py -t target_host -p port"
    print "-l --listen               - listen on [host]:[port] for"
    "                                  incoming connections"
    print "-e --excute=file_to_run   - execute the given file upon"
    "                                  receiving a connection"
    print "-c --command              - initialize a command shell"
    
usage()

```

<a name="python-start"></a>
# Script Argruments
When your script needs parameters to run or just information for the user, flags to use etc:
```
import sys

if len(sys.argv) != 2:
    print "\nUsage: csv-reader-03.py <csv file name> "
    print "\tInfo: For now it can receive 7 rows of data - hard coded"
    print "\tInfo: The Ip address field is expected to be first column\n"
    sys.exit(0)
 ```

<a name="working-with-files"></a>
# Working with Files

```
txt = open(filename) # file is opened and contents are a variable called txt
print txt.read() # print to screen

new_txt = open(filename, "ab") # append to a file
new_txt.write(add_to_file)    # add to the file the contents of variable 'add_to_file_
new_txt.write("\n")           # jump to a new line in the file
```
```
def rewind(filename):
    filename.seek(0)
def print_a_line(line_count, filename)
    print line_count, filename.readline()

```
```
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
```
<a name="functions"></a>
# Functions

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

```
# dict style
mystuff['apples']
# module style
mystuff.apples()
print mystuff.tangerine
# class style
thing = MyStuff()
thing.apples()
print thing.tangerine
```
## Syntax
```
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
   ```
By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.
https://www.tutorialspoint.com/python/python_functions.htm

- class—Tell Python to make a new kind of thing.
- object—Two meanings: the most basic kind of thing, and any instance of some thing.
- instance—What you get when you tell Python to create a class.
- def—How you define a function inside a class.
- self—Inside the functions in a class, self is a variable for the instance/object being accessed.
- inheritance—The concept that one class can inherit traits from another class, much like you and your parents.
- composition—The concept that a class can be composed of other classes as parts, much like how a car has wheels.
- attribute—A property classes have that are from composition and are usually variables.
- is-a—A phrase to say that something inherits from another, as in a “salmon” is-a “fish.”
- has-a—A phrase to say that something is composed of other things or has a trait, as in “a salmon has-a mouth.”

class X(Y) “Make a class named X that is-a Y.”

class X(object): def __init__(self, J) “class X has-a __init__ that takes self and J parameters.”

class X(object): def M(self, J) “class X has-a function named M that takes self and J parameters.”

foo = X() “Set foo to an instance of class X.”

foo.M(J) “From foo get the M function, and call it with parameters self, J.”

foo.K = Q “From foo get the K attribute, and set it to Q.”


<a name="inputs"></a>
# Inputs

```
int(raw_input())

float(raw_input())
```

<a name="for_loops"></a>

<a name="String-Formatting"></a>
# String Formatting:
```
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
```
# Loops:
for loops are traditionally used when you have a block of code which you want to repeat a fixed number of times. The Python for statement iterates over the members of a sequence in order, executing the block each time. 

```
for x in range(0, 3):
    print "We're on time %d" % (x)
    
for number in the_count:
    print "This is count %d" % number
```

<a name="color"></a>
# Python Color

```
from colorama import init, Fore, Back, Style
init(autoreset=True)
 
print Fore.RED + "FATAL ERROR! Cannot write to /boot/vmlinuz-3.2.0-33-generic"
print Back.BLUE + Fore.YELLOW + "What a cute console!"
print "This is an %simportant%s word" % (Style.BRIGHT, Style.NORMAL)
print Fore.YELLOW  + "Rosetta Code!"
print Fore.CYAN    + "Rosetta Code!"
print Fore.GREEN   + "Rosetta Code!"
print Fore.MAGENTA + "Rosetta Code!"
print Back.YELLOW + Fore.BLUE + Style.BRIGHT + " " * 40 + " == Good Bye!"
```
