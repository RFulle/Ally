# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:02:48 2019

Mad Libs

@author: RFuller
"""
import random
def printit(noun1, verb1, adj1, noun2, verb2):
       print(" Well, I was walking along the river when I saw a {}. It was really weird, because the {} was {}. Then the {} shouted: You're {}! Then {} showed up, so I {}. The End.".format(noun1, noun1, verb1, noun1, adj1, noun2, verb2))
       input()
       madlibber()
def get():
       print("Let's play Mad Libs!")
       print()
       print("Give me a noun!")
       noun1 = input()
       print()
       print("Give me a verb!")
       verb1 = input()
       print()
       print("Give me an adjective!")
       adj1 = input()
       print()
       print("Give me an proper noun!")
       noun2 = input()
       print()
       print("Give me one more verb!")
       verb2 = input()
       print()
       printit(noun1, verb1, adj1, noun2, verb2)
def madlibber():
       nouns = ['tree', 'fox', 'water', 'chair', 'motherboard', 'glass', 'dirt', 'triangle', 'hat', 'rabbit', 'cage', 'water bottle', 'speaker', 'window', 'fireplace', 'saint']
       verbs = ['run', 'walk', 'swim', 'drop', 'fly', 'compute', 'display', 'dance']
       adjectives = ['red', 'slimy', 'sturdy', 'pretty', 'hot', 'noteworthy', 'extravagant', 'legal', 'bad']
       adverbs = ['very', 'extremely', 'barely', 'bravely', 'bossily']
       print()
       print("Welcome to Mad Libber! You'll make the mad lib, I'll fill it in!")
       print("Please enter a paragraph. If you want me to fill in a word, just put it as 'noun' or 'verb' or 'adjective' or 'adverb'.")
       text = input()
       if text.find('adverb') >= 0:
              print("I see you have an adverb!")
              avct = int(text.count('adverb'))
              while avct > 0:
                     text = text.replace('adverb', random.choice(adverbs), 1)
                     avct = avct - 1
       if text.find('noun') >= 0:
              print("I see you have a noun!")
              nct = int(text.count('noun'))
              while nct > 0:
                     text = text.replace('noun', random.choice(nouns), 1)
                     nct = nct - 1
       if text.find('adjective') >= 0:
              print("I see you have an adjective!")
              ajct = int(text.count('adjective'))
              while ajct > 0:
                     text = text.replace('adjective', random.choice(adjectives), 1)
                     ajct = ajct - 1
       if text.find('verb') >= 0:
              print("I see you have a verb!")
              vct = int(text.count('verb'))
              while vct > 0:
                     text = text.replace('verb', random.choice(verbs), 1)
                     vct = vct - 1
       print("I've finished! Here's the result: ")
       print(text)
get()