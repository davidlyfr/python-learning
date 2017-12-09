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

class Terminal(object):
 
    def enter(self):
        pass

class Engine(object):

    def __init__(self,term_map):
        pass

    def play(self):
        pass

class Detected(Terminal):

    def enter(self):
        pass

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
