from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import numpy as np
import math
import imutils
import time

HEIGHT = 240
WIDTH = 180
CROPPED = int(0.3*HEIGHT)

def avg(list):
    if len(list) == 0:
        return 0
    return sum(list)/len(list)

def get_lane_angle(camera):
    rawCapture = PiRGBArray(camera, size=(240,180))
    time.sleep(0.1)
    camera.capture(rawCapture, format='bgr')
    img = rawCapture.array


    rotation_matrix = cv2.getRotationMatrix2D((HEIGHT/2, WIDTH/2), 180, 1)
    img = cv2.warpAffine(img, rotation_matrix, (HEIGHT, WIDTH))

    img = img[CROPPED:]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    cv2.imwrite('actual.jpg', img)

    #th, img = cv2.threshold(img, 85, 255, cv2.THRESH_BINARY)
    #cv2.imwrite('binary.jpg', img)
    # high_thresh, thresh_im = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # lowThresh = 0.5*high_thresh

    avging = cv2.GaussianBlur(img, (5,5), 0)
    avging = cv2.Canny(avging, 50, 150)
    #avging = cv2.Laplacian(img,cv2.CV_64F)
    #avging = np.uint8(avging)
    cv2.imwrite('canny.jpg',avging)

    # lines = cv2.HoughLines(avging, 1, np.pi/180.0, 50,50, 10)
    # lines = cv2.HoughLinesP(avging, rho=2, theta=np.pi/180, threshold=20 , minLineLength=20, maxLineGap=300)
    #lines = cv2.HoughLinesP(avging, rho=1, theta=np.pi/180, threshold=30, minLineLength=40, maxLineGap=100)
    #lines = cv2.HoughLinesP(avging,1,np.pi/180,10,80,1)
    lines = cv2.HoughLinesP(avging, rho=1, theta=np.pi/180, threshold=30, minLineLength=40, maxLineGap=100)


    blank_image = np.zeros((WIDTH,HEIGHT,3), np.uint8)
    left_slopes = []
    right_slopes = []
    avg_slope=0
    try:
        print(len(lines))
        slope = 0
        for line in lines:
            x1, y1, x2, y2  =  line[0]
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,0,255),2)
            angle = math.degrees(math.atan((y1-y2)/float(x1-x2)))
            print("one line:",angle)
            if angle < 0 :
                left_slopes.append(angle)
            else:
                right_slopes.append(angle)

        avg_slope = avg([avg(left_slopes), avg(right_slopes)])
        print(avg_slope)
        cv2.imwrite('lanes.jpg', blank_image)
        return avg_slope
    except Exception as E:
        print("no lines")
        print(E)
        return avg_slope
        # exit()


#print("original:",img.shape)
#print("lanes:",blank_image.shape)
#cv2.imwrite("lanes.jpg", blank_image)
