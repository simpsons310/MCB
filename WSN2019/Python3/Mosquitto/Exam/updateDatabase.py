import MySQLdb as giang
import json

def sensor(jsonData):
	jsonDict = json.loads(jsonData)
	blood_top = jsonDict['Blood_top']
	blood_bottom = jsonDict['Blood_bottom']
	times = jsonDict['Date']
	if(blood_bottom >= 50 and blood_bottom < 60):
		stt = "Low"
	elif(blood_bottom >= 60 and blood_bottom < 80):
		stt = "Normal"
	else:
		stt = "High"
	myDatabase = giang.connect("localhost","giang","123456","giang_db1")
	cursor = myDatabase.cursor()
	sql = """insert into blood_press(Blood_top,Blood_bottom,Stt,Time) values(%s,%s,"%s","%s")""" %(blood_top,blood_bottom,stt,times)
	print(sql)
	try:
		cursor.execute(sql)
		myDatabase.commit()
		print("Database data updated")
	except:
		print("error!")
	print("----------------------")
	print("")
	myDatabase.close()
