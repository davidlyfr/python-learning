def my_function(number):
    print number
    print "value entered %s" % number
    new_val = 5
    secon_val = 15
    print number, new_val
    return new_val, secon_val
    
def my_sec_fun(first, second):
    print "first + second as strings: " + first + second
    a = int(first)
    b = int(second)
    c = a + b
    print "a + b as integers: ", c

var_num = raw_input("Enter a number> ")
var_num2 = raw_input("Enter a number> ")
new_val, secon_val = my_function(var_num)
my_sec_fun(var_num, var_num2)

print new_val
print "\n", secon_val
