import MySQLdb as giang
import json

def sensor(jsonData):
	jsonDict = json.loads(jsonData)
	sensorID = jsonDict['Sensor_ID']
	times = jsonDict['Date']
	temp = jsonDict['Temperature']
	hum = jsonDict['Humidity']
	light = jsonDict['Light']
	dust = jsonDict['Dust']
	myDatabase = giang.connect("localhost","giang","123456","giang_db1")
	cursor = myDatabase.cursor()
	sql = """insert into MQTT(SensorID,Temperature,Humidity,Light,Dust,Time) values("%s",%s,%s,%s,%s,"%s")""" %(sensorID,temp,hum,light,dust,times)
	try:
		cursor.execute(sql)
		myDatabase.commit()
		print("Database data updated")
	except:
		print("error!")
	print("----------------------")
	print("")
	myDatabase.close()
