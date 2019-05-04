# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 09:39:00 2019

@author: rhysa
"""
import time

def notes():
       print('''
             February 2, 2019:
                    I'm starting to be suspicious of the new J.K. nuclear power factory.
                    None of the inspectors ever have any complaints about it, but it seems to me
                    like they're getting paid off. I don't have any evidence, though, so I'll continue
                    to look into this.
                    ~
                    ~ Written by Main User: Dr. Copanhaugen ~
                    ~
       ''')
       print()
       time.sleep(5)
       print()
       print('''
             February 4, 2019:
                    I'm know they're on to me. I've noticed multiple EPA violations, and I'm
                    sure I'm missing multiple more. As I was making notes of these,
                    Mr. Kampton himself actually aproached me. At first he just made small talk,
                    but then he started to ask me about my job as an inspector. He then set an open
                    suitcase full of $100 bills in front of me and said that he was sure I'd do the
                    smart thing. I left the suitcase there.
                    ~
                    ~ Written by Main User: Dr. Copanhaugen ~
                    ~
       ''')
       print()
       time.sleep(5)
       print()
       print('''
             February 5, 2019:
                    Today when I walked back to my car, there was a dead dog in front of my car.
                    The message was clear: I'll either do what Mr. Kampton wants me to, or I'll
                    end up like the dog. I'm not going to crack under the pressure, though. The
                    radioactive waste that Mr. Kampton is dumping at J. K. Factory is a threat to
                    the enviroment and all of the nearby inhabitants.
                    ~
                    ~ Written by Main User: Dr. Copanhaugen ~
                    ~
       ''')
       print()
       time.sleep(5)
       print()
       print('''
             February 6, 2019:
                    They're coming for me. I've hidden the code violations on my laptop under
                    two FolderLockers. If you're reading this, you have to unlock the first
                    FolderLocker to unlock the second FolderLocker. The code violations are
                    under the second FolderLocker. The password to the first FolderLocker
                    consists of 2 two-digit numbers and 3 words. The numbers are hidden
                    on the papers on the wall. The coordinates are:
                           West North ; South East
                     The 3 words you need are the answers to the following riddles:
                           Word #1: What has a head and a tail but no body?
                           Word #2: What has hands but can't clap?
                           Word #3: I am not alive, but I grow; I don't have lungs,
                           but I need air; I don't have a mouth, but water kills me. What am I?

                     Enter the numbers and the words in this order, no caps and no spaces:
                            number1 + Word#1 + Word#2 + Word#3 + number2
                    Open the FolderLockers, get the code, and get it to the proper authorities.
                    Good luck,
                           Dr. Copanhaugen
                    ~
                    ~ Written by Main User: Dr. Copanhaugen ~
                    ~
       ''')
       print()
       time.sleep(5)
       print()
       print("No further recent messages. Press enter twice to continue...")
       input()
       input()



def Play2():
       print("Would you like to see your previous notes? Type in 'notes' and press enter.")
       print("Otherwise, type 'write' to make new notes.")
       option = input()
       if option.lower() == 'notes':
              notes()
       elif option.lower() == 'write':
              print("Please enter the new note")
              new_note = input()
              print(new_note)
              time.sleep(5)
       else:
              print("Invalid. Please enter one or the other.")
              Play2()



def Play():
       time.sleep(.1)
       print("Welcome, Dr. Copanhaugen. Please enter your password:  ")
       password = input()
       if password.lower() != '21997659':
              print("Incorrect Password. Please check your spelling.")
              time.sleep(3)
       else:
              Play2()
Play()