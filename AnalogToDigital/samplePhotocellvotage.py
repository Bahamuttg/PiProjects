import RPi.GPIO as GPIO
import time
from pymongo import MongoClient
from datetime import datetime

def get555PulseHighTime(pin):
	counter = 0;
	GPIO.wait_for_edge(pin, GPIO.RISING);
    	while GPIO.input(pin) == GPIO.HIGH:
    		counter += 1;
    		time.sleep(0.001); # may try to change this to 0.0001 for more resolution
    	return float(counter);
		
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
print GPIO.VERSION

client = MongoClient()
db = client.luxdata
cursor = db.luxreading.find()
for document in cursor:
    print(document)
print "Currently storing " + str(db.luxreading.count()) + " records"

	
while(True):
	hightime = get555PulseHighTime(4)
	print hightime
	result = db.luxreading.insert_one( 
		{
			"millisechigh": hightime,
			"occuredtime": datetime.now()
		}
	)
	print "Entered " + str(result.inserted_id) + " in MongoDB"
	time.sleep(3);
