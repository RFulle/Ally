"""
Created on Thu Apr  4 12:51:59 2019

SimpleSnake

@author: RFuller
"""
import random, time
def dice():
       num = random.randint(1,6)
       return num
def S_():
       Stot = 0
       while 1 == 1:
              num1 = dice()
              num2 = dice()
              num3 = dice()
              print("You rolled {}, {}, and {}!".format(num1, num2, num3))
              if num1 == num2 and num2 == num3 and num1 == num3:
                     print("Darn! You lost it all!")
                     Stot = 0
                     break
              else:
                     tot = num1 * num2 * num3
                     print("You gained {} points!".format(tot))
                     Stot = Stot + tot
                     print("Your total is {}!".format(Stot))
                     print("Continue? (Y/N)")
                     cont = input()
                     if cont.lower() == 'n':
                            break
                     else:
                            print("Let's keep going!")
       print("Your total for this round was: {}".format(Stot))
       return Stot
def N_():
       Ntot = 0
       while 1 == 1:
              num1 = dice()
              num2 = dice()
              num3 = dice()
              print("You rolled {}, {}, and {}!".format(num1, num2, num3))
              if num1 == num2 and num2 == num3 and num1 == num3:
                     print("Darn! You lost it all!")
                     Ntot = 0
                     break
              else:
                     tot = num1 * num2 * num3
                     print("You gained {} points!".format(Ntot))
                     Ntot = Ntot + tot
                     print("Your total is {}!".format(Ntot))
                     print("Continue? (Y/N)")
                     cont = input()
                     if cont.lower() == 'n':
                            break
                     else:
                            print("Let's keep going!")
       print("Your total for this round was: {}".format(Ntot))
       return Ntot
def A_():
       Atot = 0
       while 1 == 1:
              num1 = dice()
              num2 = dice()
              num3 = dice()
              print("You rolled {}, {}, and {}!".format(num1, num2, num3))
              if num1 == num2 and num2 == num3 and num1 == num3:
                     print("Darn! You lost it all!")
                     Atot = 0
                     break
              else:
                     tot = num1 * num2 * num3
                     print("You gained {} points!".format(Atot))
                     Atot = Atot + tot
                     print("Your total is {}!".format(Atot))
                     print("Continue? (Y/N)")
                     cont = input()
                     if cont.lower() == 'n':
                            break
                     else:
                            print("Let's keep going!")
       print("Your total for this round was: {}".format(Atot))
       return Atot
def K_():
       Ktot = 0
       while 1 == 1:
              num1 = dice()
              num2 = dice()
              num3 = dice()
              print("You rolled {}, {}, and {}!".format(num1, num2, num3))
              if num1 == num2 and num2 == num3 and num1 == num3:
                     print("Darn! You lost it all!")
                     Ktot = 0
                     break
              else:
                     tot = num1 * num2 * num3
                     print("You gained {} points!".format(Ktot))
                     Ktot = Ktot + tot
                     print("Your total is {}!".format(Ktot))
                     print("Continue? (Y/N)")
                     cont = input()
                     if cont.lower() == 'n':
                            break
                     else:
                            print("Let's keep going!")
       print("Your total for this round was: {}".format(Ktot))
       return Ktot
def E_():
       Etot = 0
       while 1 == 1:
              num1 = dice()
              num2 = dice()
              num3 = dice()
              print("You rolled {}, {}, and {}!".format(num1, num2, num3))
              if num1 == num2 and num2 == num3 and num1 == num3:
                     print("Darn! You lost it all!")
                     Etot = 0
                     break
              else:
                     tot = num1 * num2 * num3
                     print("You gained {} points!".format(Etot))
                     Etot = Etot + tot
                     print("Your total is {}!".format(Etot))
                     print("Continue? (Y/N)")
                     cont = input()
                     if cont.lower() == 'n':
                            break
                     else:
                            print("Let's keep going!")
       print("Your total for this round was: {}".format(Etot))
       return Etot
def play():
       print("Let's play Snake!!! There are 5 rounds. Let's go to the first one!")
       time.sleep(1)
       Stot = S_()
       print("Good job! On to the next round!")
       time.sleep(1)
       Ntot = N_()
       print("Awesome! Keep it up!")
       time.sleep(1)
       Atot = A_()
       print("Great work! You're a natural!")
       time.sleep(1)
       Ktot = K_()
       print("Just one more! You can do it!")
       time.sleep(1)
       Etot = E_()
       print("That's Game!")
       time.sleep(.5)
       print("In the first round, you got {}. In the second, {}. The third was {} and the fourth was {}. The last one was {}.".format(Stot, Ntot, Atot, Ktot, Etot))
       tots = Stot + Ntot + Atot + Ktot + Etot
       print("Your grand total is {}!".format(tots))
       time.sleep(.5)
       input("Great job! Press enter to exit.")
play()