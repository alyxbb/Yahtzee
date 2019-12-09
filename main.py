import dice
import setup
scores=[]

def rollinfo(prevroll,tokeep,rollno):
  currentvalues=dice.roll(prevroll,tokeep)
  return choosetokeep(currentvalues,rollno)
def finalrollinfo(prevroll,tokeep):
  currentvalues=dice.roll(prevroll,tokeep)
  print("\non roll number 3 you get",*currentvalues)
  return currentvalues
    
def choosetokeep(currentvalues,rollno):
  print("\non roll number",rollno ,"you get",*currentvalues)
  x=input("type the numbers 1,2,3,4,5 or \ntype stop if you dont want to roll again. \nwhich ones would you like to keep?")  
  if x.upper()=="STOP":
    confirm=input("you would like to stop rolling dice. type Y to confirm or N to cancel?")
    if confirm.upper()=="Y":
      print("confirmed")
      return True,currentvalues,[]
    else:
      print("you canceled")
      return choosetokeep(currentvalues,rollno)
    
  elif len(x)==0:
    confirm=input("you would like to reroll all dice. type Y to confirm or N to cancel?")
    if confirm.upper()=="Y":
      print("confirmed")
      return False,currentvalues,[]
    else:
      print("you canceled")
      return choosetokeep(currentvalues,rollno)
  else:
    tokeep=x.split(",")
    if len(tokeep)>5:
      print("you tried to keep too many numbers")
      return choosetokeep(currentvalues,rollno)    
    else:
      newtokeep=[]
      for item in tokeep:
        try:
          newitem=int(item)
        except ValueError:
          print("invalid input")
          return choosetokeep(currentvalues,rollno)
        if newitem>5:
          print("please enter a number between 1 and 5")
          return choosetokeep(currentvalues,rollno)
        elif newitem<1:
          print("please enter a number between 1 and 5")
          return choosetokeep(currentvalues,rollno)
        elif newitem in newtokeep:
          print("please only entre each number once")
          return choosetokeep(currentvalues,rollno)
        else:
          newtokeep.append(newitem)
      print("you would like to reroll all dice but",*newtokeep,"type Y to confirm or N to cancel?",end="")
      confirm=input()
      if confirm.upper()=="Y":
        print("confirmed")
        return False,currentvalues,newtokeep
      else:
        print("you canceled")
        return choosetokeep(currentvalues,rollno)  

def printscorecard(playerno,scores):
  labels=["aces","twos","threes","fours","fives","sixes","upper sum","bonus","three of a kind","four of a kind","full house","small straight","large straight","yahtzee","chance","yahtzee bonus","lower sum","total"]
  printline()
  name=str(scores[playerno][0])
  print("|"+name+" "*(15-len(name))+"|current|possible|")
  printline()
  for item in range(len(labels)):
    printline()
    label=labels[item]
    labellen=len(label)
    labelblankchr=15-labellen
    value=str(scores[playerno][1][item])
    valuelen=len(value)
    valueblankchr=3-valuelen
    print("|"+label+" "*labelblankchr+"|  "+ value +" "*valueblankchr+"  |        |")
    if label=="bonus"or label=="lower sum" or label=="chance":
      printline()
  printline()




def printline():
  print("+---------------+-------+--------+")
def checkpossiblescores(roll):
  maxcount=0
  sum=0
  for item in roll:
    sum+=item
  for i in range(1,7):
    x=roll.count(i)
    print(x*i)
    if x>maxcount:
      maxcount=x


  if maxcount>=4:
    print(sum)
    print(sum)
  elif maxcount>=3:
    print(sum)
    print(0)
  else:
    print(0)
    print(0)

  
    
scores,players=setup.setupgame()
def scorecard(j,scores,roll):
  printscorecard(j,scores)
  checkpossiblescores(roll)
  print("YOUR FINAL ROLL:  ",*roll)
  x=input("type the exact name of the box\nwhere would you like to fill?")
  labels=["aces","twos","threes","fours","fives","sixes","three of a kind","four of a kind","full house","small straight","large straight","yahtzee","chance"]
  try:
    y=labels.index(x)
  except ValueError:
    print("invalid input")
    return scorecard(j,scores,roll)
  if 5<y:
    z=y+2

  

for i in range(13):
  for j in range(players):
    print("_"*20,"it is",str(scores[j][0])+"'s turn","_"*(24-len(scores[j][0])))
    print("\n"*5)
    stopnow,prevroll,tokeep=rollinfo([0,0,0,0,0],[0],1)
    if not stopnow:
      stopnow,prevroll,tokeep=rollinfo(prevroll,tokeep,2)
      if not stopnow:
        prevroll=finalrollinfo(prevroll,tokeep)
    scorecard(j,scores,prevroll)


    

    

