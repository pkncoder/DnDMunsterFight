import random

def test(winner, end, MunsBhp, MunsAhp, nameA, nameB):
  if MunsBhp <= 0:
    end = True
    winner = nameA
  elif MunsAhp <= 0:
    end = True
    winner = nameB
  return winner, end

def HitA(dmg, i, MunsAhitDie, rollsA):
  while i != rollsA:
      dmgroll = random.randint(1, MunsAhitDie)
      dmg += dmgroll
      i += 1
  return dmg

def HitB(dmg, i, MunsBhitDie, rollsB):
  while i != rollsB:
      dmgroll = random.randint(1, MunsBhitDie)
      dmg += dmgroll
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