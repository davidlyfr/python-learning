"""
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom is is %d" % i

    for num in numbers:
        print num
"""
# Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6)
# with a variable.
print "Pick a number = "
prompt = '>'
#set_num = int(raw_input("Pick a number: ")

set_num = raw_input(prompt)

print "Selected number is %d " % set_num

def number_list(pass_number):
    numbers = []
    print "At the top i is %d" % pass_number
    numbers.append(pass_number)

    pass_number += 1
    print "Numbers now: ", numbers
    print "At the bottom is is %d" % pass_number

    for num in numbers:
        print num
    for pints in numbers:
        print pints

print "Selected number is %d " % set_num
for i in range(0, set_num):
    number_list(i)
    i += 1

print "finished"
