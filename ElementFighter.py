import random
import time


def fight():
    print("Please give your arena name.")
    name = input()
    opponets = ["KILLER THE AWESOMESAUSCICAL", 'Tim', 'Classical Chris', 'Beth the Bestest']
    elements = ['air', 'fire', 'water', 'earth']
    opponet = random.choice(opponets)
    print("{} enters the arena....".format(opponet))
    time.sleep(1)
    print("{} and {} begin the fight!".format(name, opponet))
    time.sleep(1)
    myhealth = 40
    ophealth = 40
    while myhealth > 0 and ophealth > 0:
        opelem = random.choice(elements)
        myelem = input("Choose an element to use: Air, Fire, Earth, Water")
        print("{} used {} and {} used {}!".format(name, myelem, opponet, opelem))
        if myelem == opelem:
            print("Both {} and {} used {}! Both parties lost 5 HP.".format(name, opponet, myelem))
            myhealth = myhealth - 5
            ophealth = ophealth - 5
        elif myelem != opelem and ((myelem == 'fire' and opelem == 'air') or (myelem == "air" and opelem == 'fire')):
            print("A massive offensive barrage ensues! Both parties lose 15 HP!")
            myhealth = myhealth - 15
            ophealth = ophealth - 15
        elif myelem != opelem and ((myelem == 'water' and opelem == 'earth') or (myelem == 'earth' and opelem == 'water')):
               print("A very boring scene ensues! Everyone used offensive magic, so nothing happened at all!")
        elif myelem != opelem and (myelem == 'fire' and opelem == 'water'):
               print("You used fire, but {} blocked it with water!".format(opponet))
        elif myelem != opelem and (myelem == 'water' and opelem == 'fire'):
               print("{} used fire, but you blocked it with water!".format(opponet))

        elif myelem != opelem and (myelem == 'fire' and opelem == 'earth'):
               print("{} tried to block your attack, but couldn't completetly block it!".format(opponet))
               ophealth = ophealth - 5
        elif myelem != opelem and (myelem == 'earth' and opelem == 'fire'):
               print("You tried to block {}'s attack, but you couldn't completely block it!".format(opponet))
               myhealth = myhealth - 5
        elif myelem != opelem and ((myelem == 'air' and opelem == 'earth') or (myelem == 'earth' and opelem == 'air')):
               print("The attack by air was blocked by the use of earth!")
        elif myelem != opelem and (myelem == 'air' and opelem == 'water'):
               print("{} attacks with air, and {} could only block it partially!".format(name, opponet))
               ophealth = ophealth - 5
        elif myelem != opelem and (myelem == 'water' and opelem == 'air'):
               print("{} attacks with air, and {} could only block it partially!".format(opponet, name))
               myhealth = myhealth - 5
        elif myelem != opelem and myelem == 'lightning':
               print("{} attacks with lightning! The results are devastating for {}!!!!".format(name, opponet))
               ophealth = ophealth - 49
        elif myelem != opelem and myelem == 'ice':
               print("{} used ice! It freezes {}, allowing {} to heal!".format(name, opponet, name))
               myhealth = myhealth + 10
        print("You have {} health left and {} has {} health left.".format(myhealth, opponet, ophealth))
        if 1 == 2:
               break
    print("You have won!! Congratulations!")

































def train():
    print('')
    print('')
    print("First, the basics, Grasshopper.")
    time.sleep(random.randint(1,2))
    print("There are 4 primary elements: Fire, air, water, and earth.")
    time.sleep(random.randint(1,3))
    print("In those primary elements are two different catagories.")
    time.sleep(random.randint(1,2))
    print("The first catagory is offense. This composes of fire, air, and the combinations of such.")
    time.sleep(random.randint(1,2))
    print("The second is defensive. This is made of water, earth, and the combinations therein.")
    time.sleep(random.randint(1,2))
    print("In each round, you can choose an element to channel.")
    time.sleep(random.randint(1,2))
    print("No more talk.")
    print('''



















































    ''')
    print('ONE LEARNS THROUGH EXPERIENCE!!!')
    time.sleep(1)
    fight()

def INTERFACE():
    print("Welcome, grasshopper.")
    time.sleep(1)
    print("Would you like to go straight to the fight, or are you in need of training?")
    response = str(input()).lower()
    if response == 'fight' or response == 'f':
        print("LET THE BATTLE BEGIN!!!")
        fight()
    elif response == 'training' or response == 't':
        print("Good choice, Grasshopper.")
        time.sleep(random.randint(1,3))
        train()
    else:
        print("I'm sorry. Please respond with either 't' or 'f' or 'training' or 'fight.")
        INTERFACE()

INTERFACE()