import picamera
from subprocess import call
import os
import RPi.GPIO as GPIO
from time import time, sleep, strftime, gmtime
from multiprocessing import Process
import itertools

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SLed, GPIO.OUT)
GPIO.setup(RLed, GPIO.OUT)
GPIO.setup(ULed, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

SLed = 5
RLed = 7
ULed = 8
Button1 = 10
Button2 = 12

video_convert = "ffmpeg -r 30 -i video.h264 -vcodec copy gdrive/outputfile.mp4"


LedStandby()
while True:
    if (GPIO.input(Button1)):
    GPIO.cleanup()
    if __name__ == "__main__":
    p1 = Process(target=LedRecording)
    p1.start()
    p2 = Process(target=RecordVideo)
    p2.start()
    if (GPIO.input(Button2)): == True
      GPIO.cleanup()
      LedUploading()
      camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()
os.system('clear')
print('Recording...... \nStopping recording')

sleep(1)

#Converting the raw h.264 to mp4
call ([video_convert], shell=True)
os.system('clear')
print('Recording..............[y] \nStopping recording.....[y] \nConverting File........[y]')
print('Deleting temp files....[y]')
os.system('rm video.h264')
os.system('rm /gdrive/outputfile.mp4')
print('Uploading')
#Uploading files to google drive using rclone
os.system('rclone copy /home/pi/pythoncam/gdrive googledrive:gdrive')
os.system('clear')
print('Recording..............[y] \nStopping recording.....[y] \nConverting.............[y] \nDeleting temp files....[y] \nUploading..............[y]')
print('\nCompleted')


def LedStandby():
        for num in itertools.count(1): #creates an infinite loop
            GPIO.output(SLed, 1)
            sleep(1)
            GPIO.output(SLed, 0)
            sleep(1)


def LedRecording():
        for unm in itertools.count(1):
            GPIO.output(RLed, 1)
            sleep()
            GPIO.output(RLed, 0)
            sleep(1)


def LedUploading():
        for unm in itertools.count(1):
            GPIO.output(ULed, 1)
            sleep()
            GPIO.output(ULed, 0)
            sleep(1)
