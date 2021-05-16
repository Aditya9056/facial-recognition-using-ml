'''
This script is to apply trained model to detect guns in a video clip
Author: Jizhou Yang
'''

import urllib.request
import numpy as np
import cv2
import imutils
import datetime
import serial #Serial imported for Serial communication
import time #Required to use delay functions

serialcomm = serial.Serial('COM3',9600) 
time.sleep(2)
gun_cascade = cv2.CascadeClassifier('cascades/haarcascade_gun.xml')
myFace= []

url = 'http://192.168.137.189:8080/shot.jpg'

# initialize the first frame in the video stream
firstFrame = None

# loop over the frames of the video

gun_exist = False

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgNp, -1)

    # if the frame could not be grabbed, then we have reached the end of the video
    if not True:
        break

    # resize the frame, convert it to grayscale, and blur it
    frame = imutils.resize(frame, width=1500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    gun = gun_cascade.detectMultiScale(gray, 1.1, 5, minSize = (100, 100))
    
    if len(gun) > 15:
        gun_exist = True
        cv2.destroyAllWindows()
        print("guns detected")
        i = "alert"
        print(i)
        serialcomm.write(i.encode())
        i = input("Enter Input: ").strip()
        serialcomm.write(i.encode())
        
        
        
    for (x,y,w,h) in gun:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]    

    # if the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gray
        continue

    # draw the text and timestamp on the frame
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # show the frame and record if the user presses a key
    cv2.imshow("Security Feed", frame)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video

if gun_exist:
    print("guns detected")
else:
    print("guns NOT detected")

# cleanup the camera and close any open windows

cv2.destroyAllWindows()





