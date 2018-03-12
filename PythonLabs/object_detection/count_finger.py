import cv2
import numpy as np
from math import cos,acos,sqrt

green = ( 0x0, 0xff,  0x0)
red   = ( 0x0,  0x0, 0xff)
blue  = (0xff,  0x0,  0x0)
cnt_num = -1

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()

    cv2.rectangle(frame, (0,0), (400,400), red,0)
    crop_frame = frame[0:400,0:400]

    gray = cv2.cvtColor(crop_frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(35,35),0)
   
    _,thr = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    _,contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    #print(len(contours))
    big_cnt = 1 
    max_area= 0
    for c in range(0,len(contours)):
        cnt  = contours[c]
        area = cv2.contourArea(cnt)
        if(area > max_area):
            max_area = area
            big_cnt = c
    
    cv2.drawContours(crop_frame,contours,big_cnt,green,3)                      
    cnt = contours[big_cnt]

    
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    moments= cv2.moments(cnt)

    if(moments['m00'] != 0) :
        cx = int(moments['m10']/moments['m00'])
        cy = int(moments['m01']/moments['m00'])

    center_of_image = (cx,cy)

    cv2.circle(crop_frame,center_of_image,5,green)
    count_defects=0
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        # cos(theta) = (A**2 + B**2 - C**2)/2ABC)
        # A = sqrt((x1-x0)**2 + (y1-y0)**2)
        A = sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        B = sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        C = sqrt((end[0] - far[0])**2   + (end[1] - far[1])**2)

        
        K = ((B**2 + C**2 - A**2)/(2*B*C))
        angle = acos(K)*57
       
        if(angle<=90):
            count_defects += 1
            cv2.circle(crop_frame,far,4,red,-1)

            
    text =""    
    if(count_defects==1):
        text = "2"
    elif(count_defects==2):
        text = "3"
    elif(count_defects==3):
        text = "4"
    elif(count_defects==4):
        text = "5"
    cv2.putText(frame,text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),2,cv2.LINE_AA)                
    cv2.imshow('crop_frame',crop_frame)
    cv2.imshow('frame',frame)
    cv2.imshow('thr',thr)

    key = cv2.waitKey(10)

    if (key == 27):
        break

cam.release()
cv2.destroyAllWindows()
