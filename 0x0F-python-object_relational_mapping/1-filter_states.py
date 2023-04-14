#!/usr/bin/python3
"""
list all the scripts from the 
selected database 
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

  db = MYSQLdb.connect(host="localhost", user=argv[1], port=3306,passwd=argv[2], db=argv[3])

  cur = db.cursor()
  cur.execute("SELECT * FROM states")
  rows = cur.fetchall()

  for i in rows:
      print(i)



