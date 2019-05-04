"""
Created on Tue Apr  9 18:56:06 2019
NOTES:
       Base code for AVA, expirementing w/ MySQL adding and such.
@author: rhysa
"""

import mysql.connector

mydb = mysql.connector.connect(
              host = "localhost",
              user = "RAF",
              passwd = 'kate12312',
              database = 'ava'
              )
mycursor = mydb.cursor()


mycursor.execute("ALTER TABLE tacos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

myresult = mycursor.fetchall()

for x in myresult:
       print(x)





'''
sql = "INSERT INTO friends (name, notes) VALUES (%s, %s)"
val = [
       ('Christopher Fuller', 'STAY YEASTY'),
       ('Marcus McCarty', "Don't be Walish."),
       ('Anthony Bradshaw', "Yeah, right."),
       ("Garret Gott", "I'd totally read what you'd write."),
       ("Franklin Hopman", "Anyways")
       ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted")

'''
#mycursor.execute("CREATE TABLE friend (name VARCHAR(20), notes VARCHAR(50))")

#(ALTER TABLE people ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY)

#mycursor.execute("CREATE DATABASE people")