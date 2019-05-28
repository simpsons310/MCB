import MySQLdb as giang

myDatabase = giang.connect("localhost","giang","123456","giang_db1")
cursor = myDatabase.cursor()
cursor.execute("drop table if exists sensor1")
sql = """create table sensor1(
		ID int(5) primary key auto_increment,
		temp int(2) not null,
		hum int(2) not null,
		dust int(4) not null,
		light int(4) not null,
		Time char(30) not null)
	"""
try:
	cursor.execute(sql)
	myDatabase.commit()
	print("Table created")
except:
	print("error!")
print("")
myDatabase.close()
