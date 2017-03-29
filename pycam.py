import picamera
from time import sleep
from subprocess import call
import os

video_convert = "ffmpeg -r 30 -i video.h264 -vcodec copy outputfile.mp4"

os.system('clear')
print('Recording...')
#os.system('rm playablefile.mp4 clear')


camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
camera.start_recording('video.h264')
sleep(30)
camera.stop_recording()
os.system('clear')
print('Recording...... \nStopping recording')

sleep(1)
#os.system('DATE=$(date +"%Y-%m-%d_%H%M  ffmpeg -r 30 -i video.h264 -vcodec copy $DATE.mp4')
call ([video_convert], shell=True)
os.system('clear')
print('Recording..............[y] \nStopping recording.....[y] \nConverting File........[y]')
print('Deleting temp files....[y]')
os.system('rm video.h264')
print('\nCompleted')

