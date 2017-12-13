# exercise 45 - write your own story and convert to a game
'''
you find your self on a terminal, logged to a linux system that you are admin off - objects are:
carry out recon on your network
find a vulnerable service
brute force your entry
-- dont get too noisy
-- cover your tracks when possible

Login-own-server

what to do - nmap scan - hail mary - nessus


hacker discovered - nmap results

find services - nessus - nmap - web request

brute force choice - hydra - bree - zenmap

access denied - accessed 

'''
from sys import exit
from random import randint

class Terminal(object):
 
    def enter(self):
        print "This is the opening terminal scene for the hacker - subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self,term_map):
        self.term_map = term_map

    def play(self):
        current_scene = self.term_map.opening_term()

        while True:
            print "\n-----------"
            next_scene_name = current_scene.enter()
            current_scene = self.term_map.next_term(next_scene_name)

class Detected(Terminal):
    quote = [
        "You have been detected - IDS/IR are aware of your location..",
        "Wipe evidence, shutdown and run - detected",
        "Hope you dont server 25yrs for this - detected",
        "your foolishness has made you famous."
        ]

    def enter(self):
        print Detected.quote[randint(0, len(self.quote)-1)]
        exit(1)

class Main_Terminal(Terminal):

    def enter(self):
        pass

class FindingHosts(Terminal):

    def enter(self):
        pass

class FindingServices(Terminal):

    def enter(self):
        pass

class BruteForce(Terminal):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_term):
        pass

    def next_term(self, scene_name):
        pass

    def opening_term(self):
        pass

a_map = Map('main_terminal')
a_game = Engine(a_map)
a_game.play()
