import pytest
import ast
import sqlite3
from sqlite3 import Error
from assignment import create_connection, create_tables, create_person, create_student, select_all_students

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to select all students
def test_select_all_students():
    database = "test_pythonsqlite.db"
    create_tables(database)
    conn = create_connection(database)
    person = ('Rob', 'Thomas')
    person_id = create_person(conn, person)
    student = (person_id, 'Songwriting', '2000-01-01')
    create_student(conn, student)
    rows = select_all_students(conn)
    assert len(rows) > 0, "DMACC Student, no students were found in the database."

if __name__ == "__main__":
    pytest.main()