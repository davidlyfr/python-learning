from sys import argv

script, filename = argv

txt = open(filename)

print "Here your file %r:" % filename
print "from the script: %r" % script
print txt.read()

print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

