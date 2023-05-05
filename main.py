#! /usr/bin/python3

import requests
import random
from MunsterFightFuncs import *
from time import sleep

print("This is a simulator that has two monsters fight.")
print("This is random and will have different outputs every time!")

play = input("Would you like to customize the stats of the creature, or would you like the real stats? Real or Custom: ")
play = play.lower()

if play == 'custom':
  nameA = input("What is the first monster's name?\n")
  nameB = input("What is the second monster's name?\n")

  MunsAhp = int(input(f"What is {nameA}'s Hp?\n"))
  MunsAAC = int(input(f"What is {nameA}'s AC?\n"))
  MunsAhitDie = int(input(f"What is the hit die of {nameA}?\n"))
  rollsA = int(input("How many times will the hit die be rolled?\n"))

  MunsBhp = int(input(f"What is {nameB}'s Hp?\n"))
  MunsBAC = int(input(f"What is {nameB}'s AC?\n"))
  MunsBhitDie = int(input(f"What is the hit die of {nameB}?\n"))
  rollsB = int(input("How many times will the hit die be rolled?\n"))

  end = False
  InGameTime = 0

  winner = ()
  MunsAHit = ()
  MunsBHit = ()

  Roll = inititiveRoll()

  if Roll == 0:
    nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB = swap(nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB)

  while end == False:
    print(f"{nameA} attacts!")
    MunsAHit = random.randint(1, 20)
    
    if MunsAHit >= MunsBAC:
      print(f"{nameA} hits with a {MunsAHit}!")

      dmg = 0
      i = 0

      dmg = HitA(dmg, i, MunsAhitDie, rollsA)
      
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

      dmg = HitB(dmg, i, MunsBhitDie, rollsB)

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
  
  where = 'hit_points'
  MunsAhp = response1(where, nameA)
  where = 'armor_class'
  MunsAAC = response1(where, nameA)
  
  MunsAhitDie = int(input(f"What is the damage die for {nameA}(max amount of damage that can be done, ex. 8, or 6): "))
  rollsA = int(input(f"What is the amount of times the damage die will be rolled for {nameA}: "))

  where = 'hit_points'
  MunsBhp = response2(where, nameB)
  where = 'armor_class'
  MunsBAC = response2(where, nameB)

  MunsBhitDie = int(input(f"What is the damage die for {nameB}(max amount of damage that can be done, ex. 8, or 6): "))
  rollsB = int(input(f"What is the amount of times the damage die will be rolled for {nameB}: "))

  end = False
  InGameTime = 0

  winner = ()
  MunsAHit = ()
  MunsBHit = ()

  Roll = inititiveRoll()

  if Roll == 0:
    nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB = swap(nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB)

  while end == False:
    print(f"{nameA} attacts!")
    MunsAHit = random.randint(1, 20)
    
    if MunsAHit >= MunsBAC:
      print(f"{nameA} hits with a {MunsAHit}!")

      dmg = 0
      i = 0

      dmg = HitA(dmg, i, MunsAhitDie, rollsA)
      
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

      dmg = HitB(dmg, i, MunsBhitDie, rollsB)

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