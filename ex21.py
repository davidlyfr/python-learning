def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a ,b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multipy(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d * %d" % (a, b)
    return a / b


print "Let's do some math with just functions"

#age = add(30, 5)
print "What age are you",
age = float(raw_input())

height = subtract(78, 4)
weight = multipy(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Wight: %d, IQ: %d " % (age, height, weight, iq)

# a puzzle for the extra credit, type it in anyway
print "here is a puzzle\n"

what = add(age, subtract(height, multipy(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
