#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    def mysqlconnect(username, password, db_name):
        db = MySQLdb.connect(
            host = "localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306)

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print("{}".format(state))

        cursor.close()
        db.close()

    mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])
