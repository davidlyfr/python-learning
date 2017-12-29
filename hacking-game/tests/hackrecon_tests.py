# example python program from learning python the hardway
from nose.tools import *
from hackrecon.terminal import Terminal
from hackrecon.game import *

class Map(object):

    scenes = {
    'main_terminal': Main_Terminal(),
    'finding_services': FindingServices(),
    'detected_death': Detected(),
    'finding_hosts': FindingHosts(),
    'brute_force': BruteForce()
    }

    def __init__(self, start_term):
        self.start_term = start_term

    def next_term(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_term(self):
        return self.next_term(self.start_term)

a_map = Map('main_terminal')
a_game = Engine(a_map)
a_game.play()
