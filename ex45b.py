class Scene(object):
    def enter(self):
         print "Scene enter self"
         pass

class Engine(object):
    def __init__(self, scene_map):
        print "Engine self, scene _map"
        print "Engine scene_map set to= ", scene_map
        print "self set to =",  self
        pass

    def play(self):
        print "Engine play"
        pass

class Death(Scene):
    def enter(self):
        print "Death enter"
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        print "LaserWeaponArmory"
        pass

class TheBridge(Scene):
    def enter(self):
        print "TheBridge"
        pass

class EscapePod(Scene):
    def enter(self):
        print "enter EscapePod"
        pass

class Map(object):

    def __init__(self, start_scene):
        print "Map - self, start_scene"
        print "scene now set to ", start_scene
        pass

    def next_scene(self, scene_name):
        print "Map next_scene"
        pass

    def opening_scene(self):
        print "Map opening_scene"
        pass
print "a_map="
a_map = Map('central_corridor')
print "a_game ="
a_game = Engine(a_map)
print "a_game=", a_game
a_game.play
