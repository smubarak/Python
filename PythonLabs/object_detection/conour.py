import cv2
import numpy as np

GREEN = (0,255,0)
BLUE  = (255,0,0)
RED  = (0,0,255)
cnt_num = 0

image = cv2.imread('hand.jpg')
blurred = cv2.pyrMeanShiftFiltering(image,31,91)
gray  = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)

ret,threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

_,contours,_ = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours detected %d",len(contours))
                                         

cv2.drawContours(image,contours,cnt_num,GREEN,3)

cnt = contours[cnt_num]


# bounding rectnagle
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(image,(x,y),(x+w,y+h),BLUE,3)

# Min area bounding rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(image,[box],0,RED,2)

# min area bounding circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(image,center,radius,BLUE)


# convex defect
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

print(defects)
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start   = tuple(cnt[s][0])
    end     = tuple(cnt[e][0])
    far     = tuple(cnt[f][0])
    cv2.line(image,start,end,GREEN,1)
    cv2.circle(image,far,5,RED,-1)
    
    
    
    





cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
cv2.imshow('Display',image)
cv2.waitKey()
