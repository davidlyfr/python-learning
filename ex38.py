ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."
print ten_things
print "Only %d items" % len(ten_things)
print "                                   "

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Freisbee", "Corn", "Banshee", "Girls", "Boys"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    print stuff

print "There we go: ", stuff

print "Let's do some things with stuff"

print stuff[1]
print stuff[-1] # interesting
print ' '.join(stuff)
print '#'.join(stuff[3:5])

