from Dwarf import names
import time
import random


class Hero:

    name = ""
    health_points = 125
    attack_low = 0
    attack_high = 0

    def __init__(self):
        print("Summoning the dwarf hero...")
        time.sleep(5)
        self.name = names.names[random.randint(0, len(names.names)-1)]
        self.attack_low = random.randint(1, 11)
        self.attack_high = random.randint(11, 31)
        print("Dwarf hero name is {0}.\n{0} has attack range from {1} to {2} and {3} health.".format(self.name,
                                                                                                     self.attack_low,
                                                                                                     self.attack_high,
                                                                                                     self.health_points))
        print("*"*45)
        time.sleep(2)
