class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
# set 'happy_bday' to an instance of class Song, with list values, a, b & c

bulls_on_parade = Song(["They rally around the family", "With pockets full of ___ lol"])
# set 'bulls_on_parade' to an instance of class Song with values in a list structure

happy_bday.sing_me_a_song()
# get sing me a song function from the class set by the variable happy_bday - which has values in a list format
bulls_on_parade.sing_me_a_song()

mywords = Song(["sing me a song", "I am the piano man", "la la la"])

mywords.sing_me_a_song() 
