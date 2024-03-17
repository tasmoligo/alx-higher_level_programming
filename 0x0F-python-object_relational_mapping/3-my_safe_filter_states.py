#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connect to the database and extract required data
    """
    con_db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
    cur = con_db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %(name)s ORDER BY \
            states.id", {'name': argv[4]})
    selected = cur.fetchall()
    for datum in selected:
        print(datum)
