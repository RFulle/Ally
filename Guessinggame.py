import random
def guessinggame():
    playername = input('Please enter your name ')
    print('Welcome to the Guessing Game, {}! I will pick a number between one and a hundred, and you have to guess in 3 tries!'.format(playername))
    numnum = random.randint(1,100)
    print('OK, I have a number. What is your first guess?')
    guess1 = int(input())
    if guess1 == numnum:
        print("HOLY GUACAMOLE!!! YOU GOT IT ON YOUR FIRST GUESS! Are you a psychich or something? That's crazy! Way to go!")
        return
    elif guess1 > numnum and 39 != numnum:
        print('Nope, it is lower than that.')
    elif guess1 < numnum and 39 != numnum:
        print('Nope, it is higher than that.')
    print('Alright, time for guess number 2.')
    guess2 = int(input())
    if guess2 == numnum:
        print("Way to go! On your second try!")
        return
    elif guess2 > numnum:
        print("Not quite, it is lower than that.")
        print('One more guess left!')
    elif guess2 < numnum:
        print("Not quite, it's bigger than that.")
        print('One more guess left!')

    print("OK, time for guess number 3. This is your final guess, so do your best!")
    guess = int(input())
    if guess == numnum:
        print("We have a WINNER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("I'm afraid that's wrong.... The correct answer was {}. Better luck next time!".format(numnum))



guessinggame()
