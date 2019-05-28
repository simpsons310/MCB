import MySQLdb as giang

myDatabase = giang.connect("localhost","giang","123456","giang_db1")
cursor = myDatabase.cursor()

cursor.execute("drop table if exists led1")
cursor.execute("drop table if exists slide1")
sql = """create table sensor1(
		ID int(5) primary key auto_increment,
		temp float(5) not null,
		hum float(5) not null,
		dust float(10) not null,
		light float(10) not null,
		time char(30) not null)
	"""
sql2 = """create table led1(
		ID int(5) primary key auto_increment,
		state char(3), not null
		time char(30) not null)
	"""
try:
	cursor.execute(sql)
	cursor.execute(sql2)
	myDatabase.commit()
	print("Table created")
except:
	print("error!")
print("")
myDatabase.close()
