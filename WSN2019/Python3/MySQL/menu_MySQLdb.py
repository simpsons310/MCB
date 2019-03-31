import giang_MySQLdb as giang
import MySQLdb
import random

myDatabase = MySQLdb.connect("localhost","giang","123456","giang_db1")

def login():
	print("=============== MYSQL DATABASE ==============================")
	print("")
	print("= LOGIN INFORMATION ========")
	user = input("USER: ")
	password = input("PASSWORD: ")
	host = input("HOST: ")
	database = input("DATABASE: ")
	myDatabase = giang.login(user,password,host,database)
	return myDatabase

#myDatabase = login()

def draw_table(title,data):
	max_col = []
	for i in range (0,len(data[0])):
		maxx = 0
		for j in range (0,len(data)):
			s = str(data[j][i])
			if (maxx < len(s)):
				maxx = len(s)
		t = str(title[i])
		if (maxx < len(t)):
			maxx = len(t)
		max_col.append(maxx)
	print("+",end="")
	for i in range(0,len(max_col)):
		print("-"*(max_col[i]+1),end="")
		print("-+",end="")
	print("")
	print("|",end="")
	for i in range(0,len(max_col)):
		print(" ",end="")
		print(title[i],end="")
		t = max_col[i] - len(str(title[i]))
		print(" "*(t+1),end="")
		print("|",end="")
	print("")
	print("+",end="")
	for i in range(0,len(max_col)):
		print("-"*(max_col[i]+1),end="")
		print("-+",end="")
	print("")
	for i in range(0,len(data)):
		print("|",end="")
		for j in range(0,len(data[i])):
			print(" ",end="")
			print(data[i][j],end="")
			t = max_col[j] - len(str(data[i][j]))
			print(" "*(t+1),end="")
			print("|",end="")
		print("")	
	print("+",end="")
	for i in range(0,len(max_col)):
		print("-"*(max_col[i]+1),end="")
		print("-+",end="")
	print("")
	
def table_list():
	print("")
	results = giang.table_list(myDatabase)
	title = ["Tables list"]
	draw_table(title,results)
	
def create_table():
	print("Create table")
	table = input("Table name: ")
	num_column = int(input("Number of column: "))
	column = ""
	print("Enter column_name:")
	print("Example: Column 0: Column name")
	print("             Datatype: int(10)")
	print("")
	for i in range(0,num_column):
		column_name = input("Column %d: " %(i+1))
		column_datatype = input("   Datatype: ")
		column = column + column_name + " " + column_datatype + " not null,"
	giang.create_table(myDatabase,table,column)
	table_list()

def insert_data(table):
	print("")
	print("Insert data")
	show_table(table)
	print("")
	prop = giang.show_table_properties(myDatabase,table)
	column = ""
	value = ""
	for i in range (1,len(prop)-1):
		s = str(prop[i][0])
		val = input("%s: " %s)
		column = column + s + ","
		value = value + val + ","
	column = column[0:len(column)-1]
	value = value[0:len(value)-1]
	giang.insert_data(myDatabase,table,column,value)
	show_table(table)

def show_table(table):
	print("")
	opt = ""
	results = giang.show_table(myDatabase,table,opt)
	prop = giang.show_table_properties(myDatabase,table)
	title = []
	for i in range (0,len(prop)):
		title.append(str(prop[i][0]))
	if (len(results) == 0):
		print("Empty Set")
		return 
	draw_table(title,results)

def sort_table(table):
	print("= Sort option =======")
	print("1.Ascension")
	print("2.Descension")
	print("3.No")
	c = int(input("Select number: "))
	if (c == 1):
		opt = " asc"
	elif (c == 2):
		opt = " desc"
	else:
		opt = ""
	if (c == 1 or c == 2):
		col = input("Select column: ")
		opt = "order by " + col + opt  
	results = giang.show_table(myDatabase,table,opt)
	prop = giang.show_table_properties(myDatabase,table)
	title = []
	for i in range (0,len(prop)):
		title.append(str(prop[i][0]))
	draw_table(title,results)
	print("")

def show_table_properties(table):
	print("")
	results = giang.show_table_properties(myDatabase,table)
	title = ("Field","Type","Null","Key","Default","Extra")
	draw_table(title,results)

def insert_random(table):
	print("")
	prop = giang.show_table_properties(myDatabase,table)
	title = []
	for i in range (0,len(prop)):
		title.append(str(prop[i][0]))
	num = int(input("Number value: "))
	for k in range (0,num):
		column = ""
		value = ""
		for i in range (1,len(title)-1):
			column = column + title[i] + ","
			rand = str(random.randint(0,100))
			value = value + rand + ","
		column = column[0:len(column)-1]
		value = value[0:len(value)-1]
		giang.insert_data(myDatabase,table,column,value)
	show_table(table)

def delete_table():
	print("")
	table_list()
	print("")
	table = input("Select table: ")
	giang.delete_table(myDatabase,table)
	table_list()

def update_data(table):
	print("")
	show_table(table)
	print("")
	prop = giang.show_table_properties(myDatabase,table)
	data = ""
	ID = input("ID: ")
	for i in range (1,len(prop)-1):
		s = str(prop[i][0])
		val = input("%s: " %s)
		data = data + s + "=" + val + ","
	data = data[0:len(data)-1]
	giang.update_data(myDatabase,table,ID,data)
	show_table(table)

def delete_data(table):
	print("")
	show_table(table)
	print("")
	prop = giang.show_table_properties(myDatabase,table)
	column = []
	for i in range (0,len(prop)-1):
		column.append(str(prop[i][0]))
		print("%s" %(i+1),".","%s" %column[i])
	col = int(input("Select column: "))
	val = input("Delete value: ")
	data = column[col-1] + "=" + val
	giang.delete_data(myDatabase,table,data)
	show_table(table)

def edit_table():
	print("")
	temp = giang.table_list(myDatabase)
	row = []
	for i in range (0,len(temp)):
		row.append(str(temp[i][0]))
		print("%s" %(i+1),".","%s" %row[i])
	col = int(input("Select table: "))
	table = row[col-1]
	while True:
		print("")
		print("= Command list ===========")
		print("  1.Insert data")
		print("  2.Show table")
		print("  3.Sort table")
		print("  4.Show table properties")
		print("  5.Update data")
		print("  6.Delete data")
		print("  7.Insert random")
		print("  8.Back to command menu")
		print("  9.Exam1")
		print(" 10.Exam2")
		mode = int(input("Select command: "))
		if (mode == 1):
			insert_data(table)
		elif (mode == 2):
			show_table(table)
		elif (mode == 3):
			sort_table(table)
		elif (mode == 4):
			show_table_properties(table)
		elif (mode == 5):
			update_data(table)
		elif (mode == 6):
			delete_data(table)
		elif (mode == 7):
			insert_random(table)
		elif (mode == 8):
			break
		elif(mode == 9):
			insert_data1(table)
		elif(mode == 10):
			insert_ran20(table)
		else:
			print("Wrong input")

def insert_data1(table):
	longt = [0,1000,700,200,500,650]
	lat = [0,200,300,600,1200,500]
	sensorID = random.randint(1,5)
	light = random.randint(0,1023)
	dust = random.randint(0,10)
	AQL = random.randint(1,300)
	if (AQL > 0 and AQL <= 100):
		status = ("good")
	elif (AQL > 100 and AQL <= 200):
		status = "normal"
	else:
		status = ("bad")
	column = "sensorID,longt,lat,light,dust,AQL,status"
	value = ""
	value = value + str(sensorID) + "," + str(longt[sensorID]) + "," + str(lat[sensorID]) + "," + str(light) + "," + str(dust) + "," + str(AQL) + "," + status
	print(value)
	giang.insert_data(myDatabase,table,column,value)
	
insert_data1("Exam1")

def insert_ran20(table):
	for i in range(0,20):
		insert1_data(table);
	
def logout():
	myDatabase.close()
	login()

print("")
print("=============== MYSQL DATABASE ==============================")

while True:
	print("")
	print("= COMMAND MENU ===============")
	print("  1.Table list")
	print("  2.Create table")
	print("  3.Edit table")
	print("  4.Delete table")
	print("  5.Logout")
	print("  6.Exit")
	mode = int(input("Select command: "))
	if (mode == 1):
		table_list()
	elif (mode == 2):
		create_table()
	elif (mode == 3):
		edit_table()
	elif (mode == 4):
		delete_table()
	elif (mode == 5):
		logout()
	elif (mode == 6):
		break
	else:
		print("Wrong input")
