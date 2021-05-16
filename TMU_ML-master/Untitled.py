
# coding: utf-8

# In[4]:


import cv2
import numpy as np


# In[2]:


data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# In[3]:


myFace = []


# In[5]:


# for camera
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = data.detectMultiScale(gray, 1.3)
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),5)
            
            faceComponents = frame[y:y + h, x:x+w, :]
            fc = cv2.resize(faceComponents,(50,50))
            
            if len(myFace) < 100:
                myFace.append(fc)
            print(len(myFace))
        
        cv2.imshow('result', frame)
        if cv2.waitKey(1) == 27 or len(myFace) >= 100:
            break
    else:
        print("Camera not working")

myFace = np.asarray(myFace)
np.save('face_1.npy',myFace)
capture.release()
cv2.destroyAllWindows()

