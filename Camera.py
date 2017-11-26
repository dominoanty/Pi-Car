from picamera import PiCamera
from picamera.array import PiRGBArray
import imutils
import cv2
import time

camera = PiCamera()
camera.resolution = (240,180)
camera.framerate = 10

rawCapture = PiRGBArray(camera, size=(240,180))

time.sleep(0.1)

camera.capture(rawCapture, format='bgr')
image = rawCapture.array

cv2.imwrite("new.jpg", image)




