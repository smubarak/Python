# Create the data-set

import cv2
import numpy as np


GREEN        = (0xff,0,0)
YELLOW       = (0,0xff,0xff) 
LineWidth    = 1
sample_count = 20
sample_num   = 0

recognizer  = cv2.face.createLBPHFaceRecognizer()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera0      = cv2.VideoCapture(0)
font         = cv2.FONT_HERSHEY_SIMPLEX
users        = ['Siraj','Nusy','Lalettan']
user_id    = 0

recognizer.load('recognizer\\training_data.yml')

while True:
    # 1. Read the next frame from the camera
    ret_val,frame  = camera0.read()

    # 2. Convert the frame to  gray-scale
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 3. Get the (x,y) coordinate and (w,h) to the detected face
    face_location = face_cascade.detectMultiScale(gray_frame,1.3,5)

    
    # 4. Save the face-image to disk 
    for(x,y,h,w) in face_location:
        user_id,config = recognizer.predict(gray_frame[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),GREEN,LineWidth)
        cv2.putText(frame,users[user_id],(x,y+h), font,1,YELLOW,2,cv2.LINE_AA)
        
        sample_num+=1
        

    # 5. Show the frame
    cv2.imshow('Collecting_face_samples',frame)
    if(cv2.waitKey(1)==ord('q')):
        break
    
camera0.release()
cv2.destroyAllWindows()

print('Thank You')
    
    
