#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('test_database.db')

#create a cursor object
cursorObject = conn.cursor();

def sql_connection():
	try:
		conn = sqlite3.connect('test_db.sqlite3')
		return conn
		#print('Connection is established: Database created successfull')
	except Error:
		print (Error)
	'''
	finally:
		conn.close()
	'''

def sql_table(conn):
	cursorObject = conn.cursor()
	cursorObject.execute("CREATE TABLE IF NOT EXISTS employees (id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
	conn.commit()
	
def sql_table_insert(conn, sql_query, entities):
	cursorObject = conn.cursor()
	cursorObject.execute(sql_query, entities)
	conn.commit()
	

def sql_select(conn, sql_query):
	cursorObject =  conn.cursor()
	cursorObject.execute(sql_query)
	
conn = sql_connection()
sql_table(conn)
sql_query = "INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)"

"""
To pass values / arguments to an insert statement in the execute() method we use 

def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()
 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
sql_insert(con, entities)

"""
name = "Okechukwu"
entities = (2, name, 800, 'IT', 'Tech', '2018-02-06')
sql_table_insert(conn, sql_query, entities)
