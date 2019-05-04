# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:52:47 2019

Ally Dice

@author: RFuller
"""
import random
def rolldie1():
       sides = [1, 2, 3, 4, 5, 6]
       num1 = random.choice(sides)
       return num1

def rolldie2():
       num2 = random.randint(1,6)
       return num2

def rollboth():
       num1 = rolldie1()
       num2 = rolldie2()
       print("Die Number One came up as a {} and Die Number Two was a {}.".format(num1, num2))
       total = num1 + num2
       print("The total was {}.".format(total))
       if num1 == num2:
              print("It was doubles.")
              doubles = True
       else:
              print("It was not doubles.")
              doubles = False
       if doubles == True and num1 == 1:
              print("Snake Eyes!!!")
       else:
              print()
              input()
rollboth()