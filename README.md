# iot_project
Django server recieving data providing timestamped status of GPIO pin of esp8266

The esp8266 code for this is 

import urequests
import ujson
import machine
import time 

def send_req():
	while True:
		out = machine.Pin(16, machine.Pin.IN)
		value = out.value()
		output = ujson.dumps({'value':value})
		res = urequests.request('POST','http://sajankp.pythonanywhere.com/post', data = output)
		print(res.text)
		time.sleep(60)
