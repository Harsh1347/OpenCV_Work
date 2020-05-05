from cv2 import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",180,180,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while(True):
    #img = cv2.imread("ball.jpg")
    #cv2.imshow("balls",img)
    #cv2.waitKey(0)
    _,img = cap.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos("LH","Tracking")
    uh = cv2.getTrackbarPos("UH","Tracking")
    ls = cv2.getTrackbarPos("LS","Tracking")
    us = cv2.getTrackbarPos("US","Tracking")
    lv = cv2.getTrackbarPos("LV","Tracking")
    uv = cv2.getTrackbarPos("UV","Tracking")
    
    lb = np.array([lh,ls,lv])
    ub = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lb,ub)

    res = cv2.bitwise_or(img,img,mask = mask)
    

    cv2.imshow("balls",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.release()
cv2.destroyAllWindows()

