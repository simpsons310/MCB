import random
import datetime
import time

while True:
	print("")
	print("Time: %s" %str(datetime.datetime.now()))
	print("Temp: %s *C" %str(random.randint(20,30)))
	print("Hum: %s %%" %str(random.randint(60,90)))
	print("---------------------------------------")
	time.sleep(2)
