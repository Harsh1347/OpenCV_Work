import cv2
import numpy as np 
import pyautogui
from pynput.keyboard import Key, Controller
keyboard = Controller()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('data//output.avi', fourcc, 20.0, (1366,768))

while(True):                                
    img = pyautogui.screenshot()
    frame = np.array(img,dtype=np.uint8)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)            
    cv2.rectangle(frame,(450,385),(555,433),(0,0,255))
    frame2 = frame[385:433,450:550]
    frame2 = cv2.cvtColor(frame2,cv2.COLOR_RGB2GRAY)
    _,thresh = cv2.threshold(frame2,125,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('thresh',thresh)
    cv2.waitKey(1)
    if np.count_nonzero(thresh.ravel() == 255) > 195:
        keyboard.press(Key.space)
        print('space pressed')
        keyboard.release(Key.space)
        cv2.putText(frame,"space pressed",(500,600),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2)
    #print(np.count_nonzero(thresh.ravel() == 255))   
    out.write(frame) 
                                
out.release()                                                                                             
cv2.destroyAllWindows()                                
