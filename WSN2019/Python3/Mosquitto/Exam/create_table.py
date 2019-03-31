import MySQLdb as giang

myDatabase = giang.connect("localhost","giang","123456","giang_db1")
cursor = myDatabase.cursor()
cursor.execute("drop table blood_press")
sql = """create table blood_press(
		ID int(5) primary key auto_increment,
		Blood_top int(4) not null,
		Blood_bottom int(4) not null,
		Stt char(10) not null,
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
