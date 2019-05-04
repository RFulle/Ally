import time
import mysql.connector
def dictionary():
       print()
       word = input("Please enter a word for me to define: ")
       word = word.lower()
       sql = "SELECT * FROM vocab WHERE word LIKE '%{}%'".format(word)
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = 'kate12312',
              database = 'ava'
              )
       mycursor = mydb.cursor()
       mycursor.execute(sql)
       result = mycursor.fetchall()
       for x in result:
              print(x)
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
def happy():
       print("Sure thing")
       time.sleep(1)
       print('''
             IT'S A CELEBRATION!!!!
             YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY!
             YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY! YAY!
             ...........
...................__
............./´¯/'...'/´¯¯`·¸
........../'/.../..../......./¨¯\
........('(...´...´.... ¯~/'...')
.........\.................'...../
..........''...\.......... _.·´
............\..............(
BROFIST!''')
def talkap2(name, favcol, favnum):
       print("Data entered into database!")
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = 'kate12312',
              database = 'ava'
              )
       mycursor = mydb.cursor()
       sql = "INSERT INTO talka (name, favcol, favnum) VALUES (%s, %s, %s)"
       val = (name, favcol, favnum)
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "record inserted.")
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
def maketable():
       print()
       print("This is a restricted area. Please do not use this tool unless you are certain you know what you are doing. If you accidentally made it here, enter 0 for all the questions. Thank you.")
       if 1 == 1:
               mydb = mysql.connector.connect(
                             host = "localhost",
                             user = "RAF",
                             passwd = 'kate12312',
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
print("AVA is loading...........")
time.sleep(.3)
print("................................")
time.sleep(.2)
print("AVA online_")
while 1 == 1:
       order = input("What's up? ")
       if order.find('show') != -1:
              parse = int(order.find('show'))
              parse1 = int(parse + 5)
              parse2 = int(parse + 10)
              showthis = order[parse1:parse2]
              mydb = mysql.connector.connect(
                            host = "localhost",
                            user = "RAF",
                            passwd = 'kate12312',
                            database = 'ava'
                            )
              mycursor = mydb.cursor()
              table = showthis
              mycursor.execute("SELECT * FROM {}".format(table))
              myresult = mycursor.fetchall()
              for x in myresult:
                     print(x)
              time.sleep(1)
       if order.find("meet my friend") != -1:
                            talkap1()
                            time.sleep(1)
       if order.find('be happy for me') != -1:
              happy()
       if order.find('vocab') != -1:
              vocab()
       if order.find('dictionary') != -1:
              dictionary()
       if order.find('make table') != -1:
              maketable()
       if order.find('count') != -1:
              counter = int(input("Count to what? "))
              count = 0
              if counter >= 0:
                     while count != counter:
                            count = count + 1
                            print(count)
                            time.sleep(.3)
              else:
                     print()
       if order.find('off') != -1 or order.find('power down') != -1:
                            print("_")
                            break