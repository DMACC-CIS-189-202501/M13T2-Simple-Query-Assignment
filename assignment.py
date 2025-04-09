# TODO 1: Delete this line and add your docstring


# Import Database Information
import sqlite3
from sqlite3 import Error

# This creates a connection to the local database
def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

# This will create the table if it does not already exist
def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def create_tables(database):

    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))

def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid # returns the row id of the cursor object, the student id

def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows # return the rows

# TODO 2: Finish the select all students method
def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return:
    """


    ### YOUR CODE GOES HERE ###


if __name__ == "__main__":
    #Attempt to create tables if they don't exist
    try:
        create_tables("pythonsqlite.db")
    except:
        print("Tables may alreadyt exist")
    
    #Create some tows in the database; uncomment this and run it once
    #conn = create_connection("pythonsqlite.db")
    #with conn:
    #    person = ('Rob', 'Thomas')
    #    person_id = create_person(conn, person)

    #    student = (person_id, 'Songwriting', '2000-01-01')
    #    student_id = create_student(conn, student)
    
    # Read rows in the DB, can leave this uncommented
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)

    # TODO 3: copy the above method but modify it for select all students