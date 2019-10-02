#!/usr/bin/python3
import sqlite3

#conn = sqlite3.connect('test_database.db')

#create a cursor object
#cursorObject = conn.cursor();

"""
	menu_table(id,name, description, price)
	foodtable(id, no)
	book(id, table_no, menu_no)
"""
def main():
	conn = sql_connection()
	
	#create a cursor (handle)
	cursorObject = conn.cursor()
	cursorObject.execute("CREATE TABLE IF NOT EXISTS menu_table(id integer PRIMARY KEY AUTOINCREMENT \
	, name text, description text, price real)")

	cursorObject.execute("CREATE TABLE IF NOT EXISTS  food_table(id integer PRIMARY KEY AUTOINCREMENT \
	, table_number integer )")
	
	cursorObject.execute("CREATE TABLE IF NOT EXISTS booking(id integer PRIMARY KEY AUTOINCREMENT, \
	table_number integer, menu_number integer)")
	
	conn.commit() #commit mean make the needed changes to the database
	
	#program menu
	program_menu()
	
def program_menu():
	choice = int(input("""Select You Choice Option
	1. Add Menu
	2. View Bookings
	3. Update Menu Table
	"""))
	
	if choice == 1:
		add_menu()
	elif choice == 2:
		view_booking()
	elif choice == 3:
		update_menu_table()
	else:
		print("Unknown input")
		main()
	
def sql_connection():
	try:
		conn = sqlite3.connect('restuarant.sqlite3')
		return conn
		#print('Connection is established: Database created successfull')
	except Error:
		print (Error)
	'''
	finally:
		conn.close()
	'''

def add_menu():
	'''
	cursorObject = conn.cursor()
	cursorObject.execute(sql_query, entities)
	conn.commit()
	'''
	con = sql_connection()
	cursorObject = con.cursor()
	
	input_name = input("Enter menu name : ")
	input_description = input("Enter description for the menu : ")
	input_price = float(input("Enter menu price : "))
	'''
	get_id_query = cursorObject.execute("SELECT * FROM menu_table ORDER BY id DESC LIMIT 1;")
	rows = cursorObject.fetchall()
	
	for row in rows:
		insert_id = rows[0][0]
		print("Gotten output {0}".format(rows[0][0]) )
	#exit()
	'''
	menu_query = "INSERT INTO menu_table( name, description, price) VALUES \
	( ?, ?, ?)"
	entities = ( input_name, input_description, input_price)
	
	sql_table_insert(con, menu_query, entities)
	
	main() #kind of starting all over
	
	#entities = (input_name, input_description, input_price)
	#cursorObject.execute(menu_query, entities)
	#con.commit()
	
	'''
	
	cursorObject =  con.cursor()
	cursorObject.execute(sql_query)
	
	con = sql_connection()
	sql_table(con)
	sql_query = "INSERT INTO employees(id, name, salary, department,\
	position, hireDate) VALUES(?, ?, ?, ?, ?, ?)"
	'''
	
def update_menu_table():
	print("Inside update menu table")
	
def view_booking():
	print("Inside view booking")

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


if __name__ == "__main__":
    main()

