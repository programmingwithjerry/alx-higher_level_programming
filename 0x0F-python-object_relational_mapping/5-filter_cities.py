#!/usr/bin/python3
"""A Script that takes in the name of a state as an argument and
   lists all cities of that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db_user = argv[1]
    db_passwd = argv[2]
    database = argv[3]
    target_state = argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=db_user,
                           passwd=db_passwd,
                           db=database)
    cursor = conn.cursor()

    sql_query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """

    cursor.execute(sql_query, (target_state,))

    city_rows = cursor.fetchall()
    city_list = [city[0] for city in city_rows]

    print(', '.join(city_list))

    cursor.close()
    conn.close()

