import time
import random
import mysql.connector
#This is the "tacos" program for Ava
def convo(contx):
       print()
       #intersection for different conversations, find right conversation based on context and send there
       #If-elif chain leads to individual conversation function.
def findthread():
       print()
       #send to context
       time.sleep(.1)
       contexts = ['food', 'colors']
       contx = random.choice(contexts)
       #context = False
       convo(contx)
def throwerror(user, tal):
       print("I don't know what do with that one. I'll throw that in the error bin and take you back to where you were.")
       mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = 'kate12312',
              database = 'ava'
              )
       sql = "INSERT INTO tacos (user, errorat) VALUES (%s, %s)"
       user = user
       user.lower()
       errorat = tal
       errorat = errorat.lower()
       mycursor = mydb.cursor()
       val = (user, errorat)
       mycursor.execute(sql, val)
       mydb.commit()
       findthread()

order = input()
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
if order.find('count') != -1:
       count = 0
       while count != 10:
              count = count + 1
              print(count)
              time.sleep(1)




















