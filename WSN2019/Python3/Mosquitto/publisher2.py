import paho.mqtt.client as mqtt
import random
import json
import time
from datetime import datetime

MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "sensors"

def on_connect(client,userdata,rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))
		
def on_publish(client,userdata,mid):
	pass
def on_disconnect(client,userdata,rc):
	if rc != 0:
		pass
mqttc = mqtt.Client()
mqttc.username_pw_set(username="giang",password="123456")
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_pubhlish = on_publish
mqttc.connect(MQTT_Broker,MQTT_Port,Keep_Alive_Interval)

def publishToTopic(topic,message):
	mqttc.publish(topic,message)
	print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print("")
	
def  publishRandom():
	hum = int(random.randint(50,100))
	temp = int(random.randint(20,30))
	light = int(random.randint(0,1024))
	dust = int(random.randint(1,400))
	sensor_data = {}
	sensor_data['Sensor_ID'] = "Sensor2"
	sensor_data['Date'] = str(datetime.now())
	sensor_data['Humidity'] = hum
	sensor_data['Temperature'] = temp
	sensor_data['Light'] = light
	sensor_data['Dust'] = dust
	sensor_json_data = json.dumps(sensor_data)
	publishToTopic(MQTT_Topic,sensor_json_data)
	print("Publishing data to topic...")
	time.sleep(2)
	
while True:
	publishRandom()
	time.sleep(2)







