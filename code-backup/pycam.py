"""
StreamBox. Core file pycam.py.
Current capability: Flip camera, record raw h264 video, convert raw file to mkv or mp4, remove 
raw file (temp file), display progress.
features to add: Accept gpio input, add audio, custom/time dependent file names, syncing files 
to Google Drive (integrating Grive), making pycam.py into a service.
"""
import picamera
from time import sleep
from subprocess import call
import os

#Shell code for converting video. 
video_convert = "ffmpeg -r 30 -i video.h264 -vcodec copy outputfile.mp4"

os.system('clear')
print('Recording...')

camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
camera.start_recording('video.h264')
#30 for 30 second long video. Make it a variable for custom video length.
sleep(30)
camera.stop_recording()
os.system('clear')
print('Recording...... \nStopping recording')

sleep(1)
call ([video_convert], shell=True)
os.system('clear')
print('Recording..............[y] \nStopping recording.....[y] \nConverting File........[y]')
print('Deleting temp files....[y]')
os.system('rm video.h264')
print('\nCompleted')
