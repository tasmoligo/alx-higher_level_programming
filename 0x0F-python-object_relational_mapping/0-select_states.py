#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connect to the database and extract required data
    """
    con_db = MySQLdb.connect(host="localhost", user=argv[1],
                             port=3306, passwd=argv[2], db=argv[3])
    cur = con_db.cursor()
    cur.execute("SELECT * FROM states")
    selected = cur.fetchall()
    for datum in selected:
        print(datum)
