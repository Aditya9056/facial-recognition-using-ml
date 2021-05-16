import cv2
data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture("01 Manwa Laage (Happy New Year).mkv")
while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, None, fx=1, fy=1)
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = data.detectMultiScale(gray, 1.3)
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 5)
            cv2.imshow('result', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
            print("Camera Not Working")
capture.release()
cv2.destroyAllWindows()
