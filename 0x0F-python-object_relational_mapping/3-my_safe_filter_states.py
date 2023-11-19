#!/usr/bin/python3
"""documnetation"""
import MySQLdb
from sys import argv, exit


if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 5:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    argument = argv[4]
    #Trying to connect 
    lh = "localhost"
    pt = 3306
    dbc = MySQLdb.connect(host=lh, user=usr, password=pwd, database=db, port=pt)
    cursor = dbc.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argument,))
    states = cursor.fetchall()
    for row in states:
        print(row)

    cursor.close()
    dbc.close()
