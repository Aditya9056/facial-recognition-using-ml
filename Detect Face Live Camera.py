import cv2
import numpy as np
import time
#import serial

#arduino Code
#serialcomm = serial.Serial('COM3', 9600)

#serialcomm.timeout = 1

face1 = np.load('aditya_data.npy').reshape(100, 50*50*3)
face2 = np.load('tarun_data.npy').reshape(100,50*50*3)

users ={0:"Aditya",1:"asd"}

labels = np.zeros((200,1))
labels[:1000,:] = 0.0 #For 0 99 will have 0 and denote Aditya
labels[1000:,:] = 1.0 #For 100 to 199 will have 1 and denote shreya

data = np.concatenate([face1, face2]) #Now Data Have 0 to 199 images

def dist(x2, x1):
    return np.sqrt(((x2 -x1) **2).sum())
        
def knn(train, x, k =5):
    n = train.shape[0] #n will have 200 because data we have 200*7500
    d = []
    for i in range(n):
        d.append(dist(train[i], x))
        #print(d)
    d = np.asarray(d)
    sortIndex = np.argsort(d) #argsort sort the index rather than data
    lab = labels[sortIndex][:k] #getting 5 least distance images in lab
    count = np.unique(lab, return_counts=True) #count of 0 and 1
    return count[0][np.argmax(count[1])]

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    ret, frame = capture.read()
    if(ret == False):
        i = "all_good"
     #   serialcomm.write(i.encode())
        time.sleep(0.5)
       # print(serialcomm.readline().decode('ascii'))
        print(i)
        
    if ret:
        i = "alert"
     #   serialcomm.write(i.encode())
        time.sleep(0.5)
        #print(serialcomm.readline().decode('ascii'))
        print(i)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.4)
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255, 0), 3)
            faceComponents = frame[y:y+h, x:x+w, :]
            fc = cv2.resize(faceComponents, (50,50))
            #print(fc.shape,data.shape)
            lab = knn(data,fc.flatten())
            text = users[int(lab)]
            cv2.putText(frame, text, (x,y), font,1 , (0,255,0), 2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.imshow('result', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
            print("Camera Not Working")
#serialcomm.close()
capture.release()
cv2.destroyAllWindows()
