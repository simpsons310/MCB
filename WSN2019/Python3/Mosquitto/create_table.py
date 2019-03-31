import MySQLdb as giang

myDatabase = giang.connect("localhost","giang","123456","giang_db1")
cursor = myDatabase.cursor()
cursor.execute("drop table MQTT")
sql = """create table MQTT(
		ID int(5) primary key auto_increment,
		SensorID char(10) not null,
		Temperature int(2) not null,
		Humidity int(2) not null,
		Light int(4) not null,
		Dust int(3) not null,
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
