# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this one takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
    
# this one takes no arguments
def print_none():
	print "I have no inputs...so nothing to print"

print_two("david","lynch")
print_two_again("david", "lynch")
print_one("first")
print_none()
