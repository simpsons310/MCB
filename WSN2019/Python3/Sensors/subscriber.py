import paho.mqtt.client as mqtt
import MySQLdb as giang
import json
from datetime import datetime

MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 300
MQTT_Topic = "WSN/sensors"

def on_connect(client,userdata,flags,rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))
	client.subscribe(MQTT_Topic,0)

def on_message(client,userdata,msg):
	print("Receiving data from topic " + msg.topic)
	print("Data: " + str(msg.payload))
	sensor(msg.payload)

def sensor(jsonData):
	jsonDict = json.loads(jsonData)
	sensorID = jsonDict['SensorID']
	temp = jsonDict['Temp']
	hum = jsonDict['Hum']
	light1 = jsonDict['Light1']
	light2 = jsonDict['Light2']
	dust = jsonDict['Dust']
	times = datetime.now();
	myDatabase = giang.connect("localhost","giang","123456","giang_db1")
	cursor = myDatabase.cursor()
	sql = """insert into sensor1(temp,hum,light,dust,time) values(%s,%s,%s,%s,"%s")""" %(temp,hum,light1,dust,times)
	try:
		cursor.execute(sql)
		myDatabase.commit()
		print("Database data updated")
	except:
		print("error!")
	print("----------------------")
	print("")
	myDatabase.close()

client = mqtt.Client()
client.username_pw_set(username="giang",password="123456")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_Broker,MQTT_Port,Keep_Alive_Interval)

client.loop_forever()

