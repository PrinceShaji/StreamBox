""""
This is the final script.
Don't edit master, create a pull request
"""

import picamera
from subprocess import call
import os
import RPi.GPIO as GPIO
from time import time, sleep, strftime, gmtime

video_convert = "ffmpeg -r 30 -i video.h264 -vcodec copy outputfile.mp4"

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

