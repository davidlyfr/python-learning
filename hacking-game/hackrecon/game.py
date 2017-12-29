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
        print "nmap - Bing - Facebook (friend finder)"

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
        elif action == "Bing":
            print "detected"
            return 'detected_death'
        elif action == "Facebook":
            print "detected"
            return 'detected_death'
        else:
            print "Hard stops can be best.....!"
            print "\nTry another option "
            print " "
            return 'main_terminal'

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
            print "sudo hydra 192.168.1.70 ssh -l pi -P passwords-bad.txt -s 22 -vV"
            print "Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes."
            print " "
            print "Hydra (http://www.thc.org/thc-hydra) starting at 2017-12-18 15:47:34"
            print "[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4"
            print "[DATA] max 16 tasks per 1 server, overall 16 tasks, 500 login tries (l:1/p:500), ~32 tries per task"
            print "[DATA] attacking ssh://192.168.1.70:22/"
            print "[VERBOSE] Resolving addresses ... [VERBOSE] resolving done"
            print "[INFO] Testing if password authentication is supported by ssh://pi@192.168.1.70:22"
            print "[INFO] Successful, password authentication is supported by ssh://192.168.1.70:22"
            print "[ATTEMPT] target 192.168.1.70 - login 'pi' - pass '123456' - 1 of 500 [child 0] (0/0)"
            print "[ATTEMPT] target 192.168.1.70 - login 'pi' - pass 'password' - 2 of 500 [child 1] (0/0)"
            print "[ATTEMPT] target 192.168.1.70 - login 'pi' - pass '12345678' - 3 of 500 [child 2] (0/0)"
            print "[ATTEMPT] target 192.168.1.70 - login 'pi' - pass '1234' - 4 of 500 [child 3] (0/0)"
            print "[22][ssh] host: 127.0.0.1   login: pi   password: 34Ju90"
            print "[STATUS] attack finished for 192.168.1.70 (waiting for children to complete tests)"
            print "1 of 1 target successfully completed, 1 valid password found"
            print "Hydra (http://www.thc.org/thc-hydra) finished at 2017-12-18 15:48:11"
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

