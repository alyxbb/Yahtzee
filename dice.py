import random

def roll(prevroll,tokeep):
  dice=prevroll
  for i in range(5):
    if i+1 not in tokeep:
      dice[i]=random.randint(1,6)

  return dice