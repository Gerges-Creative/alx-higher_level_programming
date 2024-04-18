#!/usr/bin/python3

"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
import sys

if __name__ == '__main__':
    def mysqlconnect(username, password, db_name):
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

        sql_cmd = """SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id=states.id
        ORDER BY cities.id ASC"""

        cursor.execute(sql_cmd)
        states = cursor.fetchall()
        for city in states:
            print("{}".format(city))

        cursor.close()
        db.close()

    mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])