import random
#Computer plays Rock-Paper-Scissors with human player

#Computer chooses at random
r=["stone","paper","scissors"]
computer=r[random.randint(0,2)]

#take user input from keyboard
player=input("enter the choice");
if player==computer:
      print("draw")
elif player=="paper":
      if computer=="scissors":
          print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
elif player=="stone":
      if computer=="paper":
          print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
elif player=="scissors":
      if computer=="paper":
         print("lose","computer has",computer)
      else:
          print("won","computer has",computer)
