scores=[]

def numberofplayers():
  global players
  try:
    players=int(input("how many people are playing?"))
  except ValueError:
    print("please enter a whole number")
    numberofplayers()
  if players>10:
    print("you can not have more than 10 players")
    numberofplayers()
  if players<1:
    print("you must have at least one player")
    numberofplayers()

def setupgame():
  numberofplayers()
  for player in range(players):
    name=input("player "+str(player+1)+" whats your name?") 
    scores.append([name,[-1]*18])
  return scores,players