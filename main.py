import random

import time

import sys

success=0

p1score = 0

p2score = 0

restart = 0




password=int(input("If you want to play you have to give me the password to enter - "))
if password == 1905:
  time.sleep(0.1)
  success=1
   

else:
  tryagain1=input("\n"+"you got the password wrong, would you like to try again - ")
  if tryagain1 == "y" or tryagain1 == "Y" or tryagain1 == "yes" or tryagain1 == "YES" or tryagain1 == "yea" or tryagain1 == "YEA":
    time.sleep(1)
    password1=int(input("\n"+"Enter the password - "))
    if password1 == 1905:
      time.sleep(0.1)
      success=1 
    else :
      tryagain2=input("\n"+"you got the password wrong, would you like to try again - ").lower()
      if tryagain2 == "y" or tryagain2 == "Y" or tryagain2 == "yes" or tryagain2 == "YES" or tryagain2 == "yea" or tryagain2 == "YEA":
        time.sleep(1)
        password2=int(input("\n"+"Enter the password - "))
        if password2 == 1905:
          time.sleep(0.1)
          success=1 
        else:
          tryagain3=input("\n"+"you got the password wrong, would you like to try again - ").lower()
          if tryagain3 == "y" or tryagain2 == "Y" or tryagain2 == "yes" or tryagain2 == "YES" or tryagain2 == "yea" or tryagain2 == "YEA":
            time.sleep(1)
            password3=int(input("\n"+"Enter the password - "))
          if password3 == 1905:
            time.sleep(0.1)
            success=1
          else :
            print("\n"+"You have breached the ammount of password trys, your locked out for 1 minuitue")
            time.sleep(60)




print("\033[H\033[J")
sys.stdout.write("\n\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\ \n")
time.sleep(0.1)







if success==1: 
  print("\n\rWelcome to the amazing dice game\n")
  time.sleep(1)
  



print("\033[H\033[J")
player1 = input("\rWhat is your name player 1 - ")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\ ")
time.sleep(0.1)
print("\n\nOk enter ! \n")
time.sleep(1)




print("\033[H\033[J")
player2 = input("\n\rWhat is your name player 2 - ")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\")
time.sleep(0.1)
sys.stdout.write("\rloading |")
time.sleep(0.1)
sys.stdout.write("\rloading /")
time.sleep(0.1)
sys.stdout.write("\rloading -")
time.sleep(0.1)
sys.stdout.write("\rloading \\ ")
time.sleep(0.1)
print("\n\nOk enter ! \n")
time.sleep(0.5)








for rounds in range(1,6):
  restart==1
  print("\n\n***Round "+str(rounds)+"!***\n\n")
  p1dice1 = random.randint (1,6)
  p1dice2 = random.randint (1,6)

  p1total = p1dice1 + p1dice2

  p1score = p1score + p1total

  input("\nPress Enter to roll "+(player1)+"\n")
  print("\033[H\033[J")
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  print("\033[H\033[J")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)

  print("\033[H\033[J")
  print ("\n\n"+(player1)+" rolled a "+str(p1dice1)+" and a "+str(p1dice2))
  time.sleep(2)
  print ("\n"+ str(p1total) +" has been added to Player 1’s score \n")
  time.sleep(1)


  if (p1total) % 2 == 0:
    print("As your total is even, 10 more points are added!")
    p1score = p1score + 10
    time.sleep(1)
    if p1dice1 == p1dice2:
      p1dice3 = random.randint(1,6)
      p1score = p1score + p1dice3
      print("\n"+(player1)+" rolled a double, a further "+str(p1dice3)+" has been added to your score !!")
      time.sleep(1)



  else:
    print("As your total is odd, 5 points taken from your score")
    p1score = p1score-5
    if p1dice1 == p1dice2:
      p1dice3 = random.randint(1,6)
      p1score = p1score + p1dice3
      print("\n"+(player1)+" rolled a double, a further "+str(p1dice3)+" has been added to your score !!")
      time.sleep(1)
    
  if p1score<0:
    p1score=0

  print("\n"+(player1)+" score at the end of this round " +str(p1score)+"\n\n")

  time.sleep(2)
  input("\nPress Enter to roll " +(player2)+"\n")





  p2dice1 = random.randint (1,6)
  p2dice2 = random.randint (1,6)

  p2total = p2dice1 + p2dice2
  p2score = p2score + p2total
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)
  sys.stdout.write("\rRolling |")
  time.sleep(0.1)
  sys.stdout.write("\rRolling /")
  time.sleep(0.1)
  sys.stdout.write("\rRolling -")
  time.sleep(0.1)
  sys.stdout.write("\rRolling \\")
  time.sleep(0.1)



  print("\n\n\n"+(player2)+" rolled a "+str(p2dice1)+" and a "+str(p2dice2))
  time.sleep(2)
  print(str(p2total)+" has been added to "+(player2)+" score\n")
  time.sleep(1)

  if (p2total) % 2 == 0:
    print("As your total is even, 10 more points are added!")
    p2score = p2score + 10
    time.sleep(1)
    if p2dice1 == p2dice2:
      p2dice3 = random.randint(1,6)
      p2score = p2score + p2dice3
      print("\n"+(player2)+" rolled a double, a further "+str(p2dice3)+" has been added to your score !!")
      time.sleep(1)



  else:
    print("As your total is odd, 5 points taken from your score")
    p2score = p2score-5
    time.sleep(1)
    if p2dice1 == p2dice2:
      p2dice3 = random.randint(1,6)
      p2score = p2score + p2dice3
      print("\n"+(player2)+" rolled a double, a further "+str(p2dice3)+" has been added to your score !!")
      time.sleep(1)

  if p2score<0:
    p2score=0
  print("\n"+(player2)+" score at the end of this round is " +str(p2score))
  time.sleep(2)

  input("\n\nPress Enter to play the next round\n")

print("\n"+str(p1score)+" is " +(player1)+ ",s final score !")
time.sleep(3)
print("\n"+str(p2score)+" is " +(player2)+ ",s final score !")

if p1score>p2score:
	print("\n\nso"+(player1)+" wins")


elif p2score>p1score:
	print("\n\nso"+(player2)+" wins")

else:
  print("\n\ntiebreaker time !")
  time.sleep(0.5)
  sys.stdout.write("\r 1.")
  time.sleep(1)
  sys.stdout.write("\r 2.")
  time.sleep(1)
  sys.stdout.write("\r 3.")
  time.sleep(0.5)
  p1tiebreakdice = random.randint(1,6)
  p2tiebreakdice = random.randint(1,6)
  while p1tiebreakdice==p2tiebreakdice:
  	p1tiebreakdice = random.randint(1,6)
  	p2tiebreakdice = random.randint(1,6)
  if p1tiebreakdice > p2tiebreakdice:
	  print((player1)+" wins")
  elif p2tiebreakdice > p1tiebreakdice:						
    print((player2)+" wins")


print("\nWould you like to play again")
A = input ("\nYES  --  Press 1  -  \nNO  --  Press 2  -  ")
B = input("")
if A == 1 :
  restart==1
else :
  print ("\n\n\nGoodbye !")
  exit()
