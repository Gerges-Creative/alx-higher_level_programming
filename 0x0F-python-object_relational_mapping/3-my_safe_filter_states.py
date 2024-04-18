#!/usr/bin/python3

"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
import sys

if __name__ == '__main__':
    def mysqlconnect(username, password, db_name, state_name_searched):
        """
        Establishes a connection to a MySQL database and retrieves
        the IDs of states from a 'states' table.

        Args:
            username (str): The username for the MySQL database.
            password (str): The password for the MySQL database.
            db_name (str): The name of the MySQL database.

        Returns:
            None
        """
        # connect to database
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306)

        # create cursor to exec queries using SQL
        cursor = db.cursor()

        sql_cmd = """SELECT *
        FROM states
        WHERE name LIKE %s
        ORDER BY id ASC"""

        cursor.execute(sql_cmd, ('%' + state_name_searched + '%',))
        states = cursor.fetchall()
        for state in states:
            if state[1] == state_name_searched:
                print("{}".format(state))

        cursor.close()
        db.close()

    mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
