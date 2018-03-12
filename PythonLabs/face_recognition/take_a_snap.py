# Create the data-set

import cv2
import numpy as np


GREEN        = (0xff,0,0)
LineWidth    = 1
sample_count = 20
sample_num   = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera0      = cv2.VideoCapture(0)

print('Let\'s take some samples,Please Look to the camera and wait....')
user_id    = input('Enter your ID : ')


while True:
    # 1. Read the next frame from the camera
    ret_val,frame  = camera0.read()

    # 2. Convert the frame to  gray-scale
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 3. Get the (x,y) coordinate and (w,h) to the detected face
    face_location = face_cascade.detectMultiScale(gray_frame,1.3,5)

    
    # 4. Save the face-image to disk 
    for(x,y,h,w) in face_location:
        cv2.imwrite("faces/user."+ str(user_id)+"."+str(sample_num)+".jpg", gray_frame[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),GREEN,LineWidth)
        sample_num+=1
        

    # 5. Show the frame
    cv2.imshow('Collecting_face_samples',frame)
    cv2.waitKey(1)
    if(sample_num == sample_count):
        break
    
camera0.release()
cv2.destroyAllWindows()

print('Thank You')
    
    
