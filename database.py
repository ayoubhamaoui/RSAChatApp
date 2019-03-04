import sqlite3
from sqlite3 import Error
 


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM keyRSA")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def insert(conn,nom,e,d,n):
    cur = conn.cursor()
    cur.execute("insert into KeyRSA values (?, ?, ?, ?)", (nom, e, d,n))

