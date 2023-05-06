import random
import requests


def test(winner, end, MunsBhp, MunsAhp, nameA, nameB):
    if MunsBhp <= 0:
        end = True
        winner = nameA
    elif MunsAhp <= 0:
        end = True
        winner = nameB
    return winner, end


def HitA(dmg, i, MunsAhitDie, rollsA, MunsAMod):
    while i != rollsA:
        dmgroll = random.randint(1, MunsAhitDie)
        dmg += dmgroll
        dmg += MunsAMod
        i += 1
    return dmg


def HitB(dmg, i, MunsBhitDie, rollsB, MunsBMod):
    while i != rollsB:
        dmgroll = random.randint(1, MunsBhitDie)
        dmg += dmgroll
        dmg += MunsBMod
        i += 1
    return dmg


def inititiveRoll():
    rollA = random.randint(1, 20)
    rollB = random.randint(1, 20)
    if rollA > rollB or rollA == rollB:
        Roll = 1
    elif rollA < rollB:
        Roll = 0
    return Roll


def swap(nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB):
    nameA, nameB = nameB, nameA
    MunsAhp, MunsBhp = MunsBhp, MunsAhp
    MunsAAC, MunsBAC = MunsBAC, MunsAAC
    MunsAHit, MunsBHit = MunsBHit, MunsAHit
    MunsAhitDie, MunsBhitDie = MunsBhitDie, MunsAhitDie
    rollsA, rollsB = rollsB, rollsA
    return nameA, nameB, MunsAhp, MunsBhp, MunsAAC, MunsBAC, MunsAHit, MunsBHit, MunsAhitDie, MunsBhitDie, rollsA, rollsB


def get_monster(name):
    response = requests.get(f"https://www.dnd5eapi.co/api/monsters/{name}")
    return response.json()


def action_damage(input):
    if "+" not in input and "d" not in input:
        return input, 1, 0

    if "+" in input:
        input_split_1 = input.split("+")
        modifier = int(input_split_1[1])
        input = input_split_1[0]
    else:
        modifier = 0

    if "d" in input:
        damage_die = input_split_1[0]
        damage_die_split = damage_die.split("d")
        damage_die_count = int(damage_die_split[0])
        damage_die_type = int(damage_die_split[1])
    else:
        damage_die_count = 0
        damage_die_type = 0

    return damage_die_count, damage_die_type, modifier
