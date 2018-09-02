from Human import human
from Orc import orc
from Elf import elf
from Dwarf import dwarf
import random
import time

print("""
* * * * * * * * * * * * * * * * * *
* Welcome to the RPG Battle Game  *
* * * * * * * * * * * * * * * * * *

Player 1 and Player 2, choose your race
and watch your heroes fight to the death!

""")

print()

play = "y"
while play == "y":
    try:
        input_player_1 = int(input(
        """Player 1, choose your race:

(1) Human
(2) Orc
(3) Elf
(4) Dwarf

Your choice: """))
        if input_player_1 == 1:
            player1 = human.Hero()
        elif input_player_1 == 2:
            player1 = orc.Hero()
        elif input_player_1 == 3:
            player1 = elf.Hero()
        elif input_player_1 == 4:
            player1 = dwarf.Hero()
        elif input_player_1 not in range(5):
            print("Wrong input!")
            print("Assigning default race: human.")
            player1 = human.Hero()
    except ValueError:
        print("*"*45)
        print("Wrong input!")
        time.sleep(2)
        print("Assigning default race: human.")
        player1 = human.Hero()

    try:
        input_player_2 = int(input(
        """Player 2, choose your race:

(1) Human
(2) Orc
(3) Elf
(4) Dwarf

Your choice: """))
        if input_player_2 == 1:
            player2 = human.Hero()
        elif input_player_2 == 2:
            player2 = orc.Hero()
        elif input_player_2 == 3:
            player2 = elf.Hero()
        elif input_player_2 == 4:
            player2 = dwarf.Hero()
        elif input_player_2 not in range(5):
            print("Wrong input!")
            print("Assigning default race: human.")
            player2 = human.Hero()
    except ValueError:
        print("*"*45)
        print("Wrong input!")
        time.sleep(2)
        print("Assigning default race: human.")
        player2 = human.Hero()

    print("The battle beginns!")
    print("*"*45)
    time.sleep(2)

    while player1.health_points > 0 and player2.health_points > 0:
        turn = random.randint(1, 2)
        if turn == 1:
            time.sleep(2)
            print("{} tries to attack.".format(player1.name))
            time.sleep(3)
            player1_current_dmg = random.randint(player1.attack_low, player1.attack_high)
            player2.health_points -= player1_current_dmg
            print("{0} strikes {1} with {2} damage.".format(player1.name, player2.name, player1_current_dmg))
            if player2.health_points <= 0:
                time.sleep(5)
                print("*" * 45)
                print("{0} is dead. {1} has won the battle.".format(player2.name, player1.name))
                time.sleep(2)
                play = input("Play another game [y/n]: ")
            else:
                time.sleep(2)
                print("{} health is {}.".format(player2.name, player2.health_points))
                print("*" * 45)
                continue
        else:
            time.sleep(2)
            print("{} tries to attack.".format(player2.name))
            time.sleep(3)
            player2_current_dmg = random.randint(player2.attack_low, player2.attack_high)
            player1.health_points -= player2_current_dmg
            print("{0} strikes {1} with {2} damage.".format(player2.name, player1.name, player2_current_dmg))
            if player1.health_points <= 0:
                time.sleep(5)
                print("*" * 45)
                print("{0} is dead. {1} has won the battle.".format(player1.name, player2.name))
                time.sleep(2)
                play = input("Play another game [y/n]: ")
            else:
                time.sleep(2)
                print("{} health is {}.".format(player1.name, player1.health_points))
                print("*" * 45)
                continue
    if play == "y":
        continue
    elif play == "n":
        print("*"*45)
        print("Goodbye")
