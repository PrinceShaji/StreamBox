""""
This is the final script.
Don't edit master, create a pull request
"""
#How to import picam video recorder?
from subprocess import call
import os
import RPi.GPIO as GPIO
from time import time, sleep, strftime, gmtime
from multiprocessing import Process


#Have to change this with the codes to record video using picam :)
def RecordVideo():
	os.system("touch picam/hooks/start_record")


#Have to change to stop video using picam.
def StopRecording():
	os.system("touch picam/hooks/stop_record")


def ConvertVideo():
	call ([VideoConvert], shell=True)
#	os.system("ffmpeg -i /home/pi/picam/rec/archive/*.ts -c:v copy -c:a copy -bsf:a aac_adtstoasc streambox/%s.mp4" %DateFilename) 
#	call ([VideoConvert], shell=True)
#	exit()


def DeleteTempFiles():
	os.system("rm /home/pi/picam/rec/archive/*.ts")
	

def LedStandby():
#        for num in itertools.count(): #creates an infinite loop
			GPIO.output(SLed, 1)
#			sleep(1)
#			GPIO.output(SLed, 0)
#			sleep(1)
		

def LedRecording():
			GPIO.output(RLed, 1)
#			sleep(1)
#			GPIO.output(RLed, 0)
#			sleep(1)


def LedUploading():
			GPIO.output(ULed, 1)
			sleep(1)
			GPIO.output(ULed, 0)
			sleep(1)


def Main():
	while True:  #Lights standby LED until Button press.
#		GPIO.setmode(GPIO.BOARD)
#		GPIO.cleanup()
		input_state1 = GPIO.input(Button1)
		LedStandby()
		if input_state1 == False:
			GPIO.output(SLed, 0)
			break

	os.system("touch picam/rec/archive/tempfile.ts")
	DeleteTempFiles()
	RecordVideo()
	Main2()


def Main2():
	while True:
#		GPIO.setmode(GPIO.BOARD)
#		GPIO.cleanup()
		input_state2 = GPIO.input(Button2)
		LedRecording()
		if input_state2 == False:
			GPIO.output(RLed, 0)
			StopRecording()
			GPIO.output(ULed, 1)
			sleep(3)
			ConvertVideo()
			GPIO.output(ULed, 0)
			print("going to break")
			break

	Main()


DateFilename = strftime("%Y.%m.%d_%H.%M", gmtime()) 
VideoConvert = "ffmpeg -i picam/rec/archive/*.ts -c:v copy -c:a copy -bsf:a aac_adtstoasc streambox/%s.mp4" %DateFilename


#GPIO pins for LEDs
SLed = 40
RLed = 38
ULed = 37
#GPIO pins for buttons
Button1 = 10
Button2 = 12

#rand = rand.bytes(3)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SLed, GPIO.OUT) #Sets the SLed pin to output mode for lighting LED
GPIO.setup(RLed, GPIO.OUT)
GPIO.setup(ULed, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Button 1 and Button2 are set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both


try:
#	GPIO.cleanup()
	GPIO.setwarnings(False)
	Main()
except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
