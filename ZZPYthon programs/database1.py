import MySQLdb

db = MySQLdb.connect(host="localhost", user="RAF", passwd="kate12312", db="py")


cur = db.cursor()


cur.execute("SELECT * FROM py")

for row in cur.fetchall():
    print(row[0])
