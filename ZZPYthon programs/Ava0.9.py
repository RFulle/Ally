import time
import random
import mysql.connector
def GOTO():
       print()
       print("What's up?")
       print()
       com = input()
       INTER(com)
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
       GOTO()
def confuse():
       char = ['l', '1', '2', '3', '~', '//', '`', '-']
       counter = random.randint(100, 500)
       while counter >= 0:
              counter = counter - 1
              print(random.choice(char))
def dictionary():
       print()
       word = input("Please enter a word for me to define: ")
       word = word.lower()
       sql = "SELECT * FROM vocab WHERE word LIKE '%{}%'".format(word)
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = '$#PASSWORD',
              database = 'ava'
              )
       mycursor = mydb.cursor()
       mycursor.execute(sql)
       result = mycursor.fetchall()
       for x in result:
              print(x)
       GOTO()
def validate():
       print()
       print()
       passwd = input("Please enter password_ ")
       if passwd == '39':
              return True
       else:
              return False
def vocab():
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = 'kate12312',
              database = 'ava'
              )
       sql = "INSERT INTO vocab (word, definition, example) VALUES (%s, %s, %s)"
       print("What word are you defining?")
       word = input()
       word = word.lower()
       print("What's the definition of {}?".format(word))
       definition = input()
       print("Can you give me an example of {}".format(word))
       example = input()
       mycursor = mydb.cursor()
       val = (word, definition, example)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "was inserted")
def showtable():
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = '#PASSWORD',
              database = 'ava'
              )
       mycursor = mydb.cursor()
       table = input("What table to do you want to see? _")
       mycursor.execute("SELECT * FROM {}".format(table))
       myresult = mycursor.fetchall()
       for x in myresult:
              print(x)
       GOTO()
def talkap2(name, favcol, favnum):
       print("Data entered into database!")
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = '#PASSWORD',
              database = 'ava'
              )
       mycursor = mydb.cursor()
       sql = "INSERT INTO talka (name, favcol, favnum) VALUES (%s, %s, %s)"
       val = (name, favcol, favnum)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "record inserted.")
       GOTO()
def talkap1():
       print("Meet a new friend! I love new friends! What's your name?")
       name = input()
       print("So nice to meet you, {}! My name is Ava. Let's get to know each other!".format(name))
       time.sleep(1.2)
       print()
       print("What's your favorite color?")
       favcol = input()
       print("{}, really? I actually have a tie. I like the color of Aqua Aura stone and also the color Frosty Blue.".format(favcol))
       time.sleep(1.2)
       print()
       while 1 == 1:
              print("What's your favorite number? Make sure it's a number, and has no letters!")
              favnum = int(input())
              if 1 == 1:
                     print("I love {}! That being said, as a computer I love all the numbers there are.".format(favnum))
                     break
       print()
       time.sleep(.5)
       print("It was really nice to meet you, {}. I'll remember you!".format(name))
       talkap2(name, favcol, favnum)
def showtalka():
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = 'PASSWORD',
              database = 'ava'
              )
       mycursor = mydb.cursor()
       mycursor.execute("SELECT * FROM talka")
       myresult = mycursor.fetchall()
       for x in myresult:
              print(x)
def printtaco():
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = 'kate12312',
              database = 'ava'
              )
       mycursor = mydb.cursor()
       mycursor.execute("SELECT * FROM tacos")
       myresult = mycursor.fetchall()
       for x in myresult:
              print(x)
       GOTO()
def maketable():
       print()
       print("This is a restricted area.")
       passwd = validate()
       if passwd == False:
              print("INVALID PASSWORD.")
              confuse()
              exit()
       else:
               mydb = mysql.connector.connect(
                             host = "localhost",
                             user = "RAF",
                             passwd = 'PASSWORD',
                             database = 'ava'
                             )
               mycursor = mydb.cursor()
               print("What would you like to name this table?")
               table = input()
               print("Will this have 1, 2, or 3 columns?")
               num = int(input())
               if num == 1:
                      print("What's the name of the column?")
                      col1 = input()
                      mycursor.execute("CREATE TABLE {} ({} VARCHAR (255))".format(table, col1))
               elif num == 2:
                      print("What's the name of the first column?")
                      col1 = input()
                      print("What's the name of the second column?")
                      col2 = input()
                      mycursor.execute("CREATE TABLE {} ({} VARCHAR(255), {} VARCHAR(255))".format(table, col1, col2))
               elif num == 3:
                      print("What's the name of the first column?")
                      col1 = input()
                      print("What's the name of the second column?")
                      col2 = input()
                      print("What's the name of the third colmn?")
                      col3 = input()
                      mycursor.execute("CREATE TABLE {} ({} VARCHAR(255), {} VARCHAR(255), {} VARCHAR(255))".format(table, col1, col2, col3))
               GOTO()
def INTER(com):
       com = com.lower()
       if com == 'off' or com == 'power down' or com == 'stop':
              print()
              print()
       elif com == 'count off':
              print('1')
              time.sleep(.1)
              print('2')
              time.sleep(.1)
              print('3')
              time.sleep(.1)
              print('4')
              time.sleep(.1)
              print('5')
              time.sleep(.1)
              print('6')
              time.sleep(.1)
              print('7')
              time.sleep(.1)
              print('8')
              time.sleep(.1)
              print('9')
              time.sleep(.1)
              print('10')
              time.sleep(.1)
              print()
       elif com == 'show table':
              print()
              showtable()
       elif com == 'show talka':
              showtalka()
       elif com == 'meet my friend' or com == 'mmf':
              talkap1()
       elif com == 'make table':
              maketable()
       elif com == 'vocab':
              vocab()
       elif com == 'what word':
              dictionary()
       elif com == 'print taco':
              printtaco()
       elif com == 'mad lib':
              madlibber()
       else:
              print("That's not possible.")
              com = input('Try again: ')
              INTER(com)
GOTO()
'''
This was the first version of Ava, which was basically a redo of Ally. I ended it with the discovery of the find() function, which greatly improved the order capability.
4/22/2019
'''
