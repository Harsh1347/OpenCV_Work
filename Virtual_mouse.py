import cv2 as cv 
import numpy as np 
from pynput.mouse import Button,Controller
import wx

mouse = Controller()
app = wx.App(False)
(sx,sy) = wx.GetDisplaySize()
(camx,camy) = (320,240)

cam = cv.VideoCapture(0)
cam.set(3,camx)
cam.set(4,camy)

mlocold = np.array([0,0])
mouseloc = np.array([0,0])
damfac = 2.5
pinch_flag = 0
while(1):
    ret,img = cam.read()
    img = cv.GaussianBlur(img,(5,5),0)
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_img,np.array([33,80,40]),np.array([102,255,255]))

    mask_open = cv.morphologyEx(mask,cv.MORPH_OPEN,np.ones((5,5)))
    mask_close = cv.morphologyEx(mask_open,cv.MORPH_CLOSE,np.ones((20,20)))
    mask_final = mask_close

    conts,_ = cv.findContours(mask_final.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img,conts,-1,(255,0,0),3)
    if(len(conts)==2):
        if(pinch_flag==1):
            pinch_flag = 0    
            mouse.release(Button.left)
        x1,y1,w1,h1 = cv.boundingRect(conts[0])
        x2,y2,w2,h2 = cv.boundingRect(conts[1])
        #cv.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
        #cv.rectangle(img,(x2,y2),(x2+w2,y2+h2),(255,0,0),2)
        cx1 = round(x1+w1/2)
        cy1 = round(y1+h1/2)
        cx2 = round(x2+w2/2)
        cy2 = round(y2+h2/2)
        cv.line(img,(cx1,cy1),(cx2,cy2),(255,0,0),2)
        cx = round(cx1/2+cx2/2)
        cy = round(cy1/2+cy2/2)
        cv.circle(img,(cx,cy),2,(0,0,255),2)
        mouseloc = mlocold+((cx,cy)-mlocold)/damfac
        mouse.position = (round(sx - (mouseloc[0]*sx/camx)),round((mouseloc[1]*sy/camy)))
        mlocold = mouseloc
      
    elif(len(conts)==1):
        if(pinch_flag==0):
            pinch_flag = 1
            mouse.press(Button.left)
        
        x,y,w,h = cv.boundingRect(conts[0])
        #cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cx = round(x+w/2)
        cy = round(y+h/2)
        cv.circle(img,(cx,cy),20,(0,0,255),2)
        mouseloc = mlocold+((cx,cy)-mlocold)/damfac
        mouse.position = (round(sx - mouseloc[0]*sx/camx),round(mouseloc[1]*sy/camy))
        mlocold = mouseloc
        
    cv.imshow("cam",img)
    #cv.imshow("mask",mask)
    #cv.imshow("mask open",mask_open)
    cv.imshow("mask close",mask_close)
    cv.waitKey(10)
