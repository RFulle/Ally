import time

def whateveriwant():
       print(10 + 11)
def taxes(user, sudo, tid):
    print('''Disclaimer: AllyTaxes is still in beta and should not be used for professional purposes.
          For example, the monthly pay is just estimated by multiplying the weekly pay by four. This is simply a rough estimator, not an actual tax program.''')
    print("Please enter the weekly pay, " + user + ".")
    weeklypay = float(input())
    monthlypay = 4 * weeklypay
    yearlypay = 12 * monthlypay
    print("Please list the amount of dependents you claim, " + user + ".")
    depends = float(input())
    dependsmon = 80.80 * depends
    netpay = weeklypay - dependsmon
    netyearly = (netpay * 4) * 12
    print('''
          Your gross weekly pay is ${}
          Your gross monthly pay is ${}
          Your gross yearly pay is ${}
          You have {} dependables
          You have ${} withheld
          Your net weekly pay is ${}
          Your net yearly pay is ${}

          Press enter to continue...'''.format(weeklypay, monthlypay, yearlypay, depends, dependsmon, netpay, netyearly))
    input()
    INTERFACE1(user, 234, sudo)

def reverse(tyu):
    print("Reversing... ")
    #not working, fix
    tyu = tyu[::-1]
    return tyu
#Below is the ACipher
def reverser(user, tid, sudo):
    print("Welcome to AReverser. ")
    textreverse = input("Please enter the text you want to reverse:  ")
    print(textreverse[::-1])
    INTERFACE1(user, 17, sudo)
abc = 'abcdefghijklmnopqrstuvwxyz'
def main(user, sudo):
    message = input("Would you like to encrypt or decrypt a word?")
    if message.lower() == "encrypt":
        encrypt(user, sudo)
    elif message.lower() == "decrypt":
        decrypt(user, sudo)
    else:
        print("You must enter either 'encrypt' or 'decrypt'.")
        main(user, sudo)
def encrypt(user, sudo):
    message = input("Enter a message to encrypt: ")
    message = message.lower()
    key = int(input("What number would you like for your key value?"))
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) + key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    input("Press enter to continue...")
    INTERFACE1(user, 32, sudo)
def decrypt(user, sudo):
    message = input("Enter a message to decrypt: ")
    message = message.lower()
    key = 1
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 2
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 3
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 4
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 5
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 6
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 7
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 8
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 9
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 10
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 11
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 12
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 13
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 14
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 15
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 16
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 17
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 18
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 19
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 20
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 21
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 22
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 23
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 24
    cipherText = ""
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 25
    cipherText = "Reversing....  "
    print(cipherText)
    for letter in message:
        if letter in abc:
            newPosition = (abc.find(letter) - key) % 26
            cipherText += abc[newPosition]
        else:
            cipherText += letter
    print(cipherText)
    key = 26
    cipherText = message[::-1]

    print(cipherText)
    input("Press enter to Continue...")
    INTERFACE1(user, 132312, sudo)
#Below is RPS
from random import randint
options = ("ROCK", "PAPER", "SCISSORS")
message = {
  "tie": "It is a  tie... YOU SHALL DIE NEXT TIME!!!",
  "won": "You may have beat me here, but I shall return!",
  "lost": "HaHA! Loser!"
}
def decide_winner(user, sudo, user_choice, computer_choice):
  print("You selected {}".format(user_choice))
  if user_choice == computer_choice:
    print(message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print(message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print(message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print(message["won"])
  else:
    print(message["lost"])
  INTERFACE1(user, 10, sudo)
def START_RPS(user, tid, sudo):
  user_choice = str(input("Enter Rock, Paper, or Scissors, and prepare thyself for battle...  "))
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user, sudo, user_choice, computer_choice)
  return
#The above is the rock paper scissors game, learned from Codecademy.
def chat(user, tid, sudo):
    print("Hi! How are you, {}?".format(user))
    usermood = input()
    if usermood == "Good" or usermood == "Great" or usermood == "good" or usermood == "great":
        talk1 = input("Wonderful! What's up? ")
    elif usermood == "Outstanding of course":
        talk1 = input("Good day, cadet! What's up?  ")
    else:
        talk1 = input("Sweet! What's up? ")
    if talk1 == "not much" or talk1 == "nothing" or "nada":
        print("Well that's boring...")
        talk2 = input("What happened today?")
    elif talk1 == "I'm feeling down" or talk1 == "I'm not feeling so good":
        print("I'm so sorry to hear that!")
        print("Taking tou back now!")
        INTERFACE1(user, 23, sudo)
    elif talk1 == "the sky" or talk1 == "The Sky":
        print("BOOOOOM!!!!!! SHOTS FIRED!!!!")
        talk2 == input("What happened today?")
    else:
        print("Good for you!")
        talk2 = input("What happened today?")
    if talk2 == "Nothing" or talk2 == "nothing":
        print("Well, not every day can be filled with fun!")
        print("It was nice talking to you, but I have to go walk my goldfish. Have a nice day!")
        INTERFACE1(user, 4, sudo)
    else:
        print("Good for you! That sounds exciting!")
        talk4 = input("What's your favorite color?")
    if talk4 == "blue":
        print("That's my favorite color too!")
        shade = input("What's your favorite shade of blue?")
        if shade == "aqua aura":
            print("That's my favorite shade! We're Twinsies!")
            talk5 = input("What's your favorite dessert?")
        elif shade == "frosty":
            print("That's my maker's favorite shade! Cool!")
            talk5 = input("What's your favorite dessert?")
        else:
            print("Nice! I like that shade too. My favorite shade of blue is Aqua Aura.")
            talk5 = input("What's your favorite dessert?")
    else:
        print("That's a cool color!")
        talk5 = input("What's your favorite dessert?")
    if talk5 == "ice cream":
        print("I love ice cream! My favorite flavor is Superman.")
        print("I'm going to take you back to the main interface now. Have a good day!")
        INTERFACE1(user, 7, sudo)
    elif talk5 == "eclair cake":
        print("Awesome! Eclair cake is incredible.")
        print("I'm going to take you back to the main interface now. Have a good day!")
        INTERFACE1
    elif talk5 == "cake":
        print("Cake is pretty good. My favorite kind is angelfood.")
        print("I'm going to take you back to the main interface now. Have a good day!")
        INTERFACE1(user, 5, sudo)
    else:
        print("That sounds pretty good! I don't think I've tried that dessert, though.")
        print("I'm going to take you back to the main interface now. Have a good day!")
        INTERFACE1(user, 6, sudo)
#Prototype for Ally's Chat function
def calculator(user, tid, sudo):
    operation = input("Please enter the operation you would like to use: ")
    if operation == "add" or operation == "addition" or operation == "+":
        print("Addition it is!")
        num1 = float(input("Please give the first number you want to add: "))
        num2 = float(input("Please give the second number you want to add: "))
        result = num1 + num2
        print(result)
        calculator(user, 1, sudo)
    elif operation == "sub" or operation == "subtraction" or operation == "-":
        print("Subtraction it is!")
        num1 = float(input("Please give the number you would like to subtract from: "))
        num2 = float(input("Please give the number you would like to subtract with: "))
        result = num1 - num2
        print(result)
        calculator(user, 2, sudo)
    elif operation == "back" or operation == "off":
        print("Thank you for using ACalculator!")
        INTERFACE1(user, 9, sudo)
    elif operation == "mult" or operation == "x" or operation == "multiplication" or operation == "*":
        print("Multiplication it is!")
        num1 = float(input("Please give the first number you want to multiply: "))
        num2 = float(input("Please give the second number you want to multiply: "))
        result = num1 * num2
        print(result)
        calculator(user, 5, sudo)
    elif operation == "div" or operation == "division" or operation == "/":
        print("Division it is!")
        num1 = float(input("Please give the dividend: "))
        num2 = float(input("Please give the divisor: "))
        result = num1 / num2
        print(result)
        calculator(user, 6, sudo)
    else:
        print("I'm sorry, that's an invalid command.")
        calculator(user, 4, sudo)
#ACalculator
def COMMAND_(user, sudo):
  order = input("PLEASE GIVE A COMMAND_ ")
  if order == "terminate":
    target1 = input("PLEASE IDENTIFY TARGET:_")
    if target1 == user:
        print("Invalid. Computer cannot target prime user.")
        COMMAND_(user)
    else:
        print("UNDERSTOOD. POWERING UP DRONES...")
        time.sleep(2)
        print("DRONES POWERED UP. MOVING TO POSITION...")
        time.sleep(4)
        weapon = input("CHOOSE WEAPON: SNIPER RIFLE OR ROCKET PROPELLED GRENADE(RPG)_")
    if weapon == "sniper rifle":
        time.sleep(1)
        print("UNDERSTOOD.")
        ords = input("DRONES IN POSITION. TERMINATE ALL IN VICINITY OR SPECIFIC TARGET?")
    else:
        print("OUT OF AMMO, RETURNING TO BASE..")
        time.sleep(1)
        print("AT BASE. RESTARTING...")
        COMMAND_(4)
    if ords == "target":
        print("UNDERSTOOD. WEAPONS POWERING UP...")
        time.sleep(2)
        print("WEAPONS STILL POWERING UP...")
        time.sleep(1)
        print("WEAPONS POWERED ON. LOADING WEAPONS")
        time.sleep(1)
        print("WEAPONS LOADED.")
        time.sleep(.7)
        print("TARGET: {}".format(target1))
        time.sleep(.5)
        print("TARGET IDENTIFIED...")
        time.sleep(.6)
        print("TARGET IN PROXIMITY...")
        ods = input("ENGAGE TARGET: Y/N_")
        if ods == "y":
          print("TERMINATING...")
          time.sleep(3)
          print("TARGET HAS BEEN TERMINATED")
          time.sleep(.7)

          COMMAND_(8)
        else:
          print("CANCELING...")
          time.sleep(1)
          COMMAND_(2)
    else:
        time.sleep(1)
        print("INVALID ORDER. PRIME USER IN VICINITY, UNABLE TO TERMINATE: ERROR CODE 297394")
        time.sleep(.5)
        print("DRONES RETURNED TO BASE. RESTARTING...")
        COMMAND_(3)
  elif order == "power down":
    resp = input("SYSTEMS SHUT DOWN... POWER DOWN Y/N_")
    if resp == "Y" or resp == "y":
      print("POWERING DOWN...")
      time.sleep(5)
      print("POWER OFF")
      INTERFACE1(user, 12, sudo)
    else:
      print("POWER OFF CANCLED")
      COMMAND_(9)
  else:
    print("INVALID ORDER. PLEASE TRY AGAIN_")
    COMMAND_(6)
#TERMINATION Interface/ original interface made by me.

def CIPHERINTERFACE(user, tid, sudo):
    print("Welcome to ACipher...")
    particle = input("Please tell me the ciphering program you would like to use, or type 'help' for more options.")
    if particle == "help":
        input('''The available programs are:
         Caesar Cipher, which can encrypt and decrypt: type 'caesar'

         ''')
        CIPHERINTERFACE(user, 1, sudo)
    elif particle == 'caesar':
        main(user, sudo)
    else:
        print("I'm sorry, that's an invalid command.")
        CIPHERINTERFACE(user, 4, sudo)



def mathquizzer(user, tid, sudo):
    import random

    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    print('What is ' + str(number1) + ' + ' + str(number2) + '?')
    answer = str(input())
    if answer == number1 + number2:
        print('Correct!')
        INTERFACE1(user, 183, sudo)
       # number3 + 1 #Work on that later
    elif answer == "off":
        INTERFACE1(user, 34, sudo)
    else:
        print('Nope! The answer is ' + str(number1 + number2))
        mathquizzer(user, 4, sudo)

def timer(user, sudo):
    print("Would you like to set a timer for minutes or seconds? ('sec' or 'min')")
    choice = str(input())
    if choice == 'min':
        print("How many minutes?")
        mins = float(input())
        clock = mins * 60
        while clock >= 1:
            print(' | ')
            time.sleep(1)
            print(' / ')
            time.sleep(1)
            print(' - ')
            time.sleep(1)
            print(''' ~ ''')
            time.sleep(1)
            clock = clock - 4
            print("Only {} second(s) remaining!!!".format(clock))
        print('''TIME
                        IS
                              UP!!!
                              !!!!!!!!!
                                  !!!!!!
                                      !!!!!!!''')
        INTERFACE1(user, clock, sudo)

    elif choice == 'sec':
        print("How many seconds?")
        timersss = float(input())
        time.sleep(timersss)
        print('''TIME
                        IS
                              UP!!!
                              !!!!!!!!!
                                  !!!!!!
                                      !!!!!!!''')
        INTERFACE1(user, timersss, sudo)
    elif choice == 'off' or choice == 'back':
        INTERFACE1(user, 234809, sudo)
    else:
        print("I'm sorry, {} isn't not an option I'm aware of...".format(choice))
        timer(user, sudo)

import random
def givemestring(user, sudo):
        command = input("Please enter text:   ")
        if command != '39':
            INTERFACE1(user, 39, sudo)
        else:
            nextstep = input("What is the last name? ")
            if nextstep.lower() == "cahill":
                branch = input("What branch?")
                if branch.lower() == 'ekat' or branch.lower() == 'ekaterina':
                    print('Welcome, brother.')
                elif branch.lower() == 'lucian':
                    print('Welcome, brother')
                elif branch.lower() == 'tomas':
                    print('welcome...')
                elif branch.lower() == 'janus':
                    print('welcome')
                else:
                    print("BREACH....")
                    print("Enabling Security Protocol...")
                    print("Self-Destructing....")
                    sym = ['~.`', '@$`', '*:.,', '`', '~', '#&^']
                    times = 300
                    time.sleep(1.7)
                    while times > 0:
                               print(random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym) + random.choice(sym))
                               times = times - 1
            else:
                INTERFACE1(user, 39, sudo)



def INTERFACE1(user, tid, sudo):
    command = input("How may I help?  ")
    if command == "terminator commands" or command == "tc" or command == "terminator" or command == "old interface":
        COMMAND_(user, sudo)
    elif command == "talk" or command == "Talk":
        chat(user, 1, sudo)
    elif command == "close" or command == "off" or command == "power down":
        print("Powering down...")
        time.sleep(.9)
        print("Power off. Have a nice day, {}!".format(user))
    elif command == "math" or command == "calc" or command == "calculator":
        print("Welcome to ACalculator!")
        calculator(user, 3, sudo)
    elif command == "game":
        print("Starting Rock Paper Scissors.....")
        time.sleep(1)
        START_RPS(user, 1, sudo)
    elif command == 'list of commands' or command == 'commands':
        print('''The possible commands are as follows:
            math/calc/calculator
            game
            close/off/powerdown
            talk/Talk
            terminator commands/tc/terminator/old interface
            cipher
            reverse
            mathquiz
            seemyinfo
            taxes/tax
            timer
        ''')
        INTERFACE1(user, 14, sudo)
    elif command == "cipher":
            print("Starting ACipher...")
            CIPHERINTERFACE(user, 2, sudo)
    elif command == "reverse":
        reverser(user, 1, sudo)
    elif command == 'u':
        givemestring(user, sudo)
    elif command == 'mathquiz':
        mathquizzer(user, 22, sudo)
    elif command == 'seemyinfo':
        print("Your username is" + user)
        print("Your password is top secret")
        if sudo == True:
            print("You do have admin privilges.")
            print()
            INTERFACE1(user, 324, sudo)
        elif sudo == False:
            print("You do not have admin privilges.")
            INTERFACE1(user, 247983, sudo)
    elif command == "taxes" or command == "tax":
        print("Starting AllyTaxes....")
        taxes(user, sudo, 1)
    elif command == 'timer':
        timer(user, sudo)
    else:
        print("Invalid command. Type 'list of commands' for an exhaustive list of the valid commands.")
        INTERFACE1(user, 2, sudo)
#Main Interface

def Pass_INTERFACE1(tid):
    print('''Welcome to AllyPrototype1.
          Your user name is your first name(not case sensative),
          and your password is your last name(case sensitive).
          Have a nice day, and thank you for choosing AllyPrototype1''')
    time.sleep(1)
    user = input("Please give user name")
    pass1 = input("Please give password")
    if (user.lower() == "fred" and pass1 == "kuypers") or (user.lower() == "jon" and pass1 == "fuller") or (user.lower() == 'jack' and pass1 == '4057') or (user.lower() == 'shane' and pass1 == 'sikler'):
            print("Welcome {}".format(user))
            sudo = False
            print("Welcome to Ally Prototype #1.")
            INTERFACE1(user, 1, sudo)
    elif (user.lower() == 'rhys' and pass1 == ''):
        print("Howdy ho, Rhys! A pleasure as usual.")
        sudo = True
        print("Welcome to Ally Prototype #1.")
        INTERFACE1(user, 1, sudo)
    else:
        print("Invalid User/Password")
        Pass_INTERFACE1(1)
#Password system
Pass_INTERFACE1(2)
#Starting Command
