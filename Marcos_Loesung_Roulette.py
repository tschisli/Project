import random
import time
budget = 1000
betin = 0
betmoney = 0
allred = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
allblack = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
allfirstcolumn = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
allsecondcolumn = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
previousnumbers = []
randomsentences = ["Good Luck!", "I hope you're going to win!", "I believe in you!!!", "Wish you good luck!", "Good luck...", "Good game!", "I hope you'll win!", "Let the game begin!"]
randomsentences2 = ["Nice, the Bullet stopped at the right Number!", "Your gambling was perfect!!", "Well played!!", "WOW!!!", "Nice gambling!!", "Congrats!!", "Nice, good choice!", "Good for you!!", "Congratulation!!", "OMG, so Lucky!"]

print("Welcome to the Roulette game!")
print("\n-----------------")
print("You start with a Budget of 1000 $")
print('\n' * 2)
while budget > 0:
  land = random.randint(0, 36)
  input("Press Enter to see the Table of possible Bets.")
  print('\n' * 2)
  print("The following Bets are possible: \n----------------------")
  print("Enter '1' if you want to bet on a specific Number!\nEnter '2' if you want to bet on a red Number!\nEnter '3' if you want to bet on a black Number!\nEnter '4' if you want to bet on odd Numbers!\nEnter '5' if you want to bet on even Numbers!\nEnter '6' if you want to bet on Numbers between 1 and 18!\nEnter '7' if you want to bet on Numbers between 19 and 36!\nEnter '8' if you want to bet on Numbers between 1 and 12!\nEnter '9' if you want to bet on Numbers between 13 and 24!\nEnter '10' if you want to bet on Numbers between 25 and 36!\nEnter '11' if you want to bet on the first column!\nEnter '12' if you want to bet on the second column!\nEnter '13' if you want to bet on the third column!")
  print("\n----------------------")

  answerbet = input("Enter your Bet: ")
  print('\n')
  print("Your Current Budget: ", budget)
  print("The previous Numbers are:", previousnumbers)

  def play():
    global land
    global betmoney
    global budget
    budget -= betmoney
    print('\n' * 3)
    print("The Bullet is spinning.....")
    print('\n')
    time.sleep(3)
    random1 = random.randint(0, 36)
    print("The Bullet just passed Number", random1, "...")
    time.sleep(2)
    random2 = random.randint(0, 36)
    print("The Bullet nearly stopped at Number", random2, "...")
    time.sleep(2)
    print("THE BULLET LANDS ON NUMBER", land, "!")
    previousnumbers.append(land)
    time.sleep(2)

  def lose():
    global betmoney
    global budget
    print("Oh no, you lost! Unlucky!")
    time.sleep(2)
    print("You lost", betmoney, "$...")
    print('\n')
    time.sleep(1)
    print("Your Budget is now", budget, "$!")

  def win(num):
    global betmoney
    global budget
    print(random.choice(randomsentences2))
    time.sleep(2)
    wincash = (betmoney * num) - betmoney
    print("You just won", wincash, "$!!!")
    budget += wincash + betmoney
    print('\n')
    time.sleep(1)
    print("Your Budget is now", budget, "$!")

  def getamount(num1, multi):
    sentences_for_gametype = ["", "You chose to bet on a specific Number... You are a gambler!", "You chose to bet on the color red...", "You chose to bet on the color black...", "You chose to bet on odd Numbers...", "You chose to bet on even Numbers...", "You chose to bet on Numbers between 1 and 18...", "You chose to bet on Numbers between 19 and 36...", "You chose to bet on Numbers between 1 and 12...", "You chose to bet on Numbers between 13 and 24...", "You chose to bet on Numbers between 25 and 36...", "You chose to bet on the first column...", "You chose to bet on the second column...", "You chose to bet on the third column..."]
    print('\n')
    global betmoney
    global budget
    global betin
    print(sentences_for_gametype[num1])

    if num1 == 1:
      while True:
        betin = input("Enter lucky Number: ")
        try:
          betin = int(betin)
        except:
          print("Error - This Number does not exist! Enter agian... ")
        else:
          if betin < 0 or betin > 36:
            print("In Roulette you only can bet on Numbers between 0 and 36. Check your Input.")
          else:
            while True:
              betmoney = input("How much money do you want to spend?: ")
              try:
                betmoney = int(betmoney)
              except:
                print("Error - Please only enter Integer Numbers.")
              else:
                if budget >= betmoney:
                  print("If the Bullet lands on number", betin, "you win", (betmoney * multi) - betmoney, "$!")
                  print('\n' * 2)
                  print(random.choice(randomsentences))
                  time.sleep(1)
                  break
                else:
                  print("You don't have enough budget to play with that amount of money... enter again!")
            break
    else:
      while True:
        betmoney = input("How much money do you want to spend?: ")
        try:
          betmoney = int(betmoney)
        except:
          print("Error - Please only enter Integer Numbers.")
        else:
          if budget >= betmoney:
            print("Possible win:", (betmoney * multi) - betmoney, "$!")
            print('\n' * 2)
            print(random.choice(randomsentences))
            time.sleep(1)
            break
          else:
            print("You don't have enough budget to play with that amount of money... enter again!")

  if answerbet <= "13":
    if answerbet == "1":
      getamount(1, 36)
    if answerbet == "2":
      getamount(2, 2)
    if answerbet == "3":
      getamount(3, 2)
    if answerbet == "4":
      getamount(4, 2)
    if answerbet == "5":
      getamount(5, 2)
    if answerbet == "6":
      getamount(6, 2)
    if answerbet == "7":
      getamount(7, 2)
    if answerbet == "8":
      getamount(8, 3)
    if answerbet == "9":
      getamount(9, 3)
    if answerbet == "10":
      getamount(10, 3)
    if answerbet == "11":
      getamount(11, 3)
    if answerbet == "12":
      getamount(12, 3)
    if answerbet == "13":
      getamount(13, 3)

    play()

    if answerbet == "1" and betin == land:
      win(36)
    if answerbet == "1" and betin != land:
      lose()
    if answerbet == "2" and land in allred:
      win(2)
    if answerbet == "2" and land not in allred:
      lose()
    if answerbet == "3" and land in allblack:
      win(2)
    if answerbet == "3" and land not in allblack:
      lose()
    if answerbet == "4" and land % 2 != 0:
      win(2)
    if answerbet == "4" and land % 2 == 0:
      lose()
    if answerbet == "5" and land % 2 == 0:
      win(2)
    if answerbet == "5" and land % 2 != 0:
      lose()
    if answerbet == "6" and land <= 18:
      win(2)
    if answerbet == "6" and land > 18:
      lose()
    if answerbet == "7" and land >= 19:
      win(2)
    if answerbet == "7" and land < 19:
      lose()
    if answerbet == "8" and land <= 12:
      win(3)
    if answerbet == "8" and land > 12:
      lose()
    if answerbet == "9" and land in range(13, 25):
      win(3)
    if answerbet == "9" and land not in range(13, 25):
      lose()
    if answerbet == "10" and land >= 25:
      win(3)
    if answerbet == "10" and land < 25:
      lose()
    if answerbet == "11" and land in allfirstcolumn:
      win(3)
    if answerbet == "11" and land not in allfirstcolumn:
      lose()
    if answerbet == "12" and land in allsecondcolumn:
      win(3)
    if answerbet == "12" and land not in allsecondcolumn:
      lose()
    if answerbet == "13" and land % 3 == 0:
      win(3)
    if answerbet == "13" and land % 3 != 0:
      lose()
  else:
    print("Please choose numers from 1 to 13\n")
print("You lost all your Money...")
