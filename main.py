#! /usr/bin/python3

import random
from MunsterFightFuncs import *

print("This is a simulator that has two monsters fight either with your own stats, or using \
       Wizards of the Coasts stats of their monsters. The link that this is using for stats, \
       is within this API: https://www.dnd5eapi.co/")
print("This is random and will have different outputs every time!")

play = input(
    "Would you like to customize the stats of the creature, or would you like the real stats? Real or Custom: ")
play = play.lower()

if play == 'custom':
    nameA = input("What is the first monster's name?\n")
    nameB = input("What is the second monster's name?\n")

    MunsAhp = int(input(f"What is {nameA}'s Hp?\n"))
    MunsAAC = int(input(f"What is {nameA}'s AC?\n"))
    MunsAhitDie = int(input(f"What is the possible max dammage of {nameA}?\n"))
    rollsA = int(input("How many times will the damage die be rolled?\n"))
    MunsAMod = int(input(f"What is the modifier of {nameA}'s attacks?\n"))

    MunsBhp = int(input(f"What is {nameB}'s Hp?\n"))
    MunsBAC = int(input(f"What is {nameB}'s AC?\n"))
    MunsBhitDie = int(input(f"What is the possible max dammage of {nameB}?\n"))
    rollsB = int(input("How many times will the damage die be rolled?\n"))
    MunsBMod = int(input(f"What is the modifier of {nameB}'s attacks?\n"))

    end = False
    InGameTime = 0

    winner = ()
    MunsAHit = ()
    MunsBHit = ()

    Roll = inititiveRoll()

    if Roll == 0:
        nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB = swap(
            nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB)

    while end == False:
        print(f"{nameA} attacts!")
        MunsAHit = random.randint(1, 20)

        if MunsAHit >= MunsBAC:
            print(f"{nameA} hits with a {MunsAHit}!")

            dmg = 0
            i = 0

            dmg = HitA(dmg, i, MunsAhitDie, rollsA, MunsAMod)

            print(f'Damage is {dmg}!')
            MunsBhp -= dmg

        else:
            print(f"{nameA} did not hit with a {MunsAHit}. Sad.")

        print(f"{nameB} = {MunsBhp}")
        print(f"{nameA} = {MunsAhp}")
        input("Press the enter key to continue...")

        print(f"{nameB} attacts!")
        MunsBHit = random.randint(1, 20)

        if MunsBHit >= MunsAAC:
            print(f"{nameB} hit with a {MunsBHit}.")

            dmg = 0
            i = 0

            dmg = HitB(dmg, i, MunsBhitDie, rollsB, MunsBMod)

            print(f"Dmg is {dmg}")
            MunsAhp -= dmg

        else:
            print(f"{nameB} did not hit with a {MunsBHit}.")

        InGameTime += 6
        winner, end = test(winner, end, MunsBhp, MunsAhp, nameA, nameB)

        print(f"{nameB} = {MunsBhp}")
        print(f"{nameA} = {MunsAhp}")
        input("Press the enter key to continue...")

    print("There is a winner!")
    print(f"The winner is {winner}!")
    print(f"That took {InGameTime} seconds in game.")
    print(f"In other words that took {InGameTime / 60} minute(s).")
elif play == 'real':
    nameA = input("What is the first monster's name?\n")
    nameB = input("What is the second monster's name?\n")

    monsterA = get_monster(name=nameA)
    monsterB = get_monster(name=nameB)

    MunsAhp = monsterA["hit_points"]
    MunsAAC = monsterA["armor_class"][0]["value"]

    rollsA, MunsAhitDie, MunsAMod = action_damage(
        monsterA["actions"][0]["damage"][0]["damage_dice"])
    rollsB, MunsBhitDie, MunsBMod = action_damage(
        monsterB["actions"][0]["damage"][0]["damage_dice"])

    MunsBhp = monsterB["hit_points"]
    MunsBAC = monsterB["armor_class"][0]["value"]

    end = False
    InGameTime = 0

    winner = ()
    MunsAHit = ()
    MunsBHit = ()

    Roll = inititiveRoll()

    if Roll == 0:
        nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB = swap(
            nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB)

    while end == False:
        print(f"{nameA} attacts!")
        MunsAHit = random.randint(1, 20)

        if MunsAHit >= MunsBAC:
            print(f"{nameA} hits with a {MunsAHit}!")

            dmg = 0
            i = 0

            dmg = HitA(dmg, i, MunsAhitDie, rollsA, MunsAMod)

            print(f'Damage is {dmg}!')
            MunsBhp -= dmg

        else:
            print(f"{nameA} did not hit with a {MunsAHit}. Sad.")

        print(f"{nameB} = {MunsBhp}")
        print(f"{nameA} = {MunsAhp}")
        input("Press the enter key to continue...")

        print(f"{nameB} attacts!")
        MunsBHit = random.randint(1, 20)

        if MunsBHit >= MunsAAC:
            print(f"{nameB} hit with a {MunsBHit}.")

            dmg = 0
            i = 0

            dmg = HitB(dmg, i, MunsBhitDie, rollsB, MunsBMod)

            print(f"Dmg is {dmg}")
            MunsAhp -= dmg

        else:
            print(f"{nameB} did not hit with a {MunsBHit}.")

        InGameTime += 6
        winner, end = test(winner, end, MunsBhp, MunsAhp, nameA, nameB)

        print(f"{nameB} = {MunsBhp}")
        print(f"{nameA} = {MunsAhp}")
        input("Press the enter key to continue...")

    print("There is a winner!")
    print(f"The winner is {winner}!")
    print(f"That took {InGameTime} seconds in game.")
    print(f"In other words that took {InGameTime / 60} minute(s).")
