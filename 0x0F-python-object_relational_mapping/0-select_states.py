#!/usr/bin/python3



if __name__ == "__main__":
    import MYSQLdb
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(1)
    usr = argv[1]
    pwd = argv[2]
    db = argv[3]
    #Trying to connect 
    db_connection = MySQLdb.connect(usr=usr, passwd="", db ="hbtn_0e_0_usa",port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for row in states:
        print(row)

    cursor.close()
    db_connection.close()