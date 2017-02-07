import ibmiotf.device
import json
import time
import signal
from time import sleep
import random
import sys
options = {

	"org": "vy8sg5",
	"type": "intellisoft-sample",
	"id": "intellisoftsample1",
	"auth-method": "token",
	"auth-token": "testdevice"
}

def myCommandCallback(cmd):
	print('inside command callback')
	print cmd
### Let's try and make our exits graceful ###
def signal_handler(signal, frame):

	print('You pressed Ctrl+C!')
	signal.signal(signal.SIGINT, signal_handler)

### Main routine starts here ###

def myCommandCallback(cmd):
	print('inside command callback')
	print cmd

def main():
	client = ibmiotf.device.Client(options)
	client.connect()
	client.commandCallback = myCommandCallback

	while True:
		try:
			t = time.time()
			json_data = {}
			json_data["Time"] = t
			json_data["Sensor1"] = random.randint(1,1023)
			myPayload = json_data
			client.publishEvent("status","json", myPayload)
			print myPayload
	    	except SystemExit :
	        	break
	    	except:
	        # print t, val
	        	print "Unexpected error:", sys.exc_info()
		sleep(1)

if __name__ == "__main__":

   	main()