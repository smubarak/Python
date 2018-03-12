# Harr cascade

import cv2
import numpy as np

GREEN = (255,0,0)
BLUE  = (0,255,0)
Thickness = 1

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier('haarcascade_eye.xml')

cap =cv2.VideoCapture(0)

while True:
    ret,img  = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,h,w) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),GREEN,Thickness)
        rio_gray  = gray[y:y+h,x:x+w]
        rio_color = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(rio_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(rio_color,(ex,ey),(ex+ew,ey+eh),BLUE,Thickness)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    print(k)
    if(k==27):
        break
cap.release()
cv2.destroyAllWindows()
    
    
