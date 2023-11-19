#!/usr/bin/python3
"""documnetation"""
import MySQLdb
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    cities = []
    argument = argv[4]
    #Trying to connect 
    lh = "localhost"
    pt = 3306
    dbc = MySQLdb.connect(host=lh, user=usr, password=pwd, database=db, port=pt)
    cursor = dbc.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
     WHERE states.name = %s ORDER BY id ASC"""
    cursor.execute(query, (argument,))
    rows = cursor.fetchall()
    for row in rows:
        cities.append(row[1])
    print(', '.join(cities))
    cursor.close()
    dbc.close()
