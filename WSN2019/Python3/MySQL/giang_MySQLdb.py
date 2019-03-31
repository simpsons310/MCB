import MySQLdb
import datetime

myDatabase = MySQLdb.connect("localhost","giang","123456","giang_db1")

#----Function----
def login(user,password,host,database):
	myDatabase = MySQLdb.connect("%s" %host,"%s" %user,"%s" %password,"%s" %database)
	return myDatabase

def table_list(myDatabase):
	cursor = myDatabase.cursor()
	sql = """show tables"""
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		return results
	except:
		return "Empty!"
	
def create_table(myDatabase,table,column):
	cursor = myDatabase.cursor()
	sql = """create table %s(
			ID int(10) primary key auto_increment,
			%s
			Time datetime not null
			)
		""" %(table,column)
	try:
		cursor.execute(sql)
	except:
		print("Error!")

def delete_table(myDatabase,table):
	cursor = myDatabase.cursor()
	sql = """drop table %s""" %table
	try:
		cursor.execute(sql)
	except:
		print("Error!")

def insert_data(myDatabase,table,column,value):
	cursor = myDatabase.cursor()
	column = column + ",Time"
	value = value + ",'%s'" %str(datetime.datetime.now())
	sql = """insert into %s(%s) values(%s)""" %(table,column,value)
	try:
		cursor.execute(sql)
		myDatabase.commit()
	except:
		print("Error!")
		myDatabase.rollback()

def show_table(myDatabase,table,opt):
	cursor = myDatabase.cursor()
	sql = """select * from %s %s""" %(table,opt)
	cursor.execute(sql)
	results = cursor.fetchall()
	return results

def show_table_properties(myDatabase,table):
	cursor = myDatabase.cursor()
	sql = """DESC %s""" %(table)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		return results
	except: 
		return "Empty table!"

def update_data(myDatabase,table,ID,data):
	cursor = myDatabase.cursor()
	sql = """UPDATE %s SET %s WHERE id=%s""" %(table,data,ID)
	try:
		cursor.execute(sql)
		myDatabase.commit()
	except:
		myDatabase.rollback()
		print("Error!")

def delete_data(myDatabase,table,ID):
	cursor = myDatabase.cursor()
	sql = """DELETE FROM %s WHERE %s""" %(table,ID)
	try:
		cursor.execute(sql)
		myDatabase.commit()
	except:
		myDatabase.rollback()
		print("Error!")	

myDatabase.close()

###############################################################################


