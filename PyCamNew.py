""""
This is the final script.
Don't edit master, create a pull request
"""

import picamera
from subprocess import call
import os
import RPi.GPIO as GPIO
from time import time, sleep, strftime, gmtime
from multiprocessing import Process
import itertools

video_convert = "ffmpeg -r 30 -i video.h264 -vcodec copy outputfile.mp4" 
#video_convert = "ffmpeg -r 30 -i video.h264 -vcodec copy %s.mp4" %DateFilename

DateFilename=strftime("%Y-%m-%d %H:%M", gmtime())

def RecordVideo():
	camera = picamera.PiCamera()
    camera.hflip = True
    camera.vflip = True
    camera.start_recording('video.h264')

    #Define StopRecording so that that can be done with another
    #button input
    #sleep(5)
    #camera.stop_recording()


def StopRecording():
	camera = picamera.PiCamera()
	camera.stop_recording()


def ConvertVideo():
	call ([video_convert], shell=True)
	exit()


def RenameFile():
	os.renames("outputfile.mp4" "gdrive/%s.mp4" %DateFilename)


def DeleteTempFiles():
	os.remove("video.h264")
	os.remove("outputfile.mp4")


def UploadFiles():
	command = ([rclone copy /gdrive/ googledrive:gdrive/])
	result = subprocess.Popen(command)
	result.communicate()	

	"""
	command = ([RCLONE, 'move', '--log-file=rclone_upload.log', '--transfers', RCLONE_TRANSFERS, '--drive-chunk-size=16M', '--exclude', 'filepart', LOCAL_DIR + dir + '/', REMOTE_NAME  + REMOTE_DIR + dir + '/'])
    result = subprocess.Popen(command)
    result.communicate()
    """


def LedStandby():
	GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)
    for num in itertools.count(1): #creates an infinite loop
        GPIO.output(40,1)
        sleep(1)
        GPIO.output(40,0)
        sleep(1)





if __name__ == "__main__":   #start of the program?        
