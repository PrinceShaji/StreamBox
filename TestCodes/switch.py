import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN)
GPIO.setup(40, GPIO.OUT)

try:
	while True:
		if GPIO.input(5):
		   GPIO.output(40, 1)

		else:
		   GPIO.output(40, 0) 	

		 sleep (0.1)   
finally:
     GPIO.cleanup()

     		 
