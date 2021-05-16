import urllib.request
import cv2
import numpy as np

data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
myFace= []
#capture = cv2.VideoCapture(0)
url = 'http://192.168.137.102:8080/shot.jpg'
while True:
#    ret, frame = capture.read(1)
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgNp, -1)
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = data.detectMultiScale(gray, 1.3)
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 5)
            faceComponents = frame[y:y + h, x:x+w, :]
            fc = cv2.resize(faceComponents,(50,50))

            if len(myFace)<= 500:
                myFace.append(fc)
            print(len(myFace))

        cv2.imshow('result',frame)
        if cv2.waitKey(1) == 27 or len(myFace)>=500:
            break
    else:
        print("Camera Not Working")
myFace = np.asarray(myFace)
np.save('aditya_data.npy',myFace)


import matplotlib.pyplot as plt
myFace.shape

plt.imshow(myFace[15])
plt.show()


