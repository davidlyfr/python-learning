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
        print "You are logged in as Root on your own terminal."
        print "The first step in any journey, is to go in the "
        print "right direction."
        print " "
        print "Recon - find your target"
        print "you now wear a Black-Hat - hacking a remote pc"
        print "is your objective - lets find it! how?"
        print "what tool do you use to find the target?"
        print "nmap - Bing - Facebook friend finder"

        action = raw_input("> ")
  
        if action == "nmap":
            print "Good decision"
            print " "
#            print "Nmap scan report for 192.168.1.70"
#            print "Host is up (0.0012s latency)."
#            print "Not shown: 995 closed ports"
#            print "PORT     STATE SERVICE"
#            print "22/tcp   open  ssh"
#            print "139/tcp  open  netbios-ssn"
#            print "445/tcp  open  microsoft-ds"
#            print "5050/tcp open  mmcc"
#            print "5666/tcp open  nrpe"
#            print "MAC Address: B8:27:EB:B3:3E:CB (Raspberry Pi Foundation)"
#            print " "
#            print "Nmap done: 1 IP address (1 host up) scanned in 5.95 seconds"
            return 'finding_hosts'
        elif action == "hail mary":
            print "detected"
            return 'detected_death'
        elif action == "nessus":
            print "detected"
            return 'detected_death'
        

class FindingHosts(Terminal):

    def enter(self):
        print "Lets Ping scan the network,"
        print "to find out the IP of neighboring hosts"
        print "What is the correct parameter in the following line"
        print "nmap -XX 192.168.1.0/24"
        print " sn sN sV "

        action = raw_input("> ")
        
        if  action == "sn":
            print "Good decision"
            print " "
            print "$ nmap -sn 192.168.1.0/24"
            print "Starting Nmap 6.40 ( http://nmap.org ) at 2017-12-17 21:28 UTC"
            print "Nmap scan report for 192.168.1.12"
            print "Host is up (0.00086s latency)."
            print "Nmap scan report for 192.168.1.70 - Rasp VPN"
            print "Host is up (0.00046s latency)."
            print "Nmap scan report for 192.168.1.111"
            print "Host is up (0.018s latency)."
            print "Nmap scan report for router.asus.com (192.168.1.254)"
            print "Host is up (0.0085s latency). "
            print "Nmap done: 1 IP address (1 host up) scanned in 5.95 seconds"
            print "Nmap done: 256 IP addresses (3 hosts up) scanned in 7.73 seconds"
            return 'brute_force'
        elif action == "sN":
            print "detected"
            return 'detected_death'
        elif action == "sV":
            print "detected"
            return 'detected_death'
        else:
            print "Does not ring a bell!"
            return 'finding_hosts'
class FindingServices(Terminal):

    def enter(self):
        print "What tool is best for finding services? "
        print "nmap - google - sans"
        
        action = raw_input("> ")
 
        if action == "nmap":
            print "Starting Nmap 6.40 ( http://nmap.org ) at 2017-12-17 19:40 UTC"
            print "Nmap scan report for 192.168.1.70"
            print "Host is up (0.0012s latency)."
            print "Not shown: 995 closed ports"
            print "PORT     STATE SERVICE"
            print "22/tcp   open  ssh"
            print "139/tcp  open  netbios-ssn"
            print "445/tcp  open  microsoft-ds"
            print "5050/tcp open  mmcc"
            print "5666/tcp open  nrpe"
            print "MAC Address: B8:27:EB:B3:3E:CB (Raspberry Pi Foundation)"
            print " "
            print "Nmap done: 1 IP address (1 host up) scanned in 5.95 seconds"
            return 'brute_force'
        elif action == "hail mary":
            print "detected"
            return 'detected_death'
        elif action == "nessus":
            print "detected"
            return 'detected_death'
        else:
            print "Try again!"
            return 'finding_services'

class BruteForce(Terminal):

    def enter(self):
        print "We have chosen to attach the SSH protocol."
        print "This type of attack requires parameters."
        print "It finds authorised users, names and passwords."
        print "Chose a tool - zenmap - hydra - passive DNS"

        action = raw_input("> ")

        if action == "hydra":
            print "Hydra starting --- winner"
            exit(1)
        elif action == "zenmap":
            print "This tool is a graphical version of nmap - that we just used."
            print "Try again"
            return 'brute_force'
        elif action == "passive dns":
            print "na - this tool is more for gathering information"
            print "that may lead to a target of interest -"
            print "like - Matching an SQL db to an IP"
            return 'brute_force'
        else:
            print "try again- though you maybe right"
            print "There are no straight lines in IT"
            return 'brute_force'

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
