import cv2
import numpy as np
from playsound import playsound
# LB = 'Drum' 
# cv2.putText(img, LB, (x, y), font, 1,  (255, 255, 0),  2)  

font = cv2.FONT_HERSHEY_TRIPLEX 
def mouse_event(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        if x>200 and x < 310 and y > 200 and y < 310:            
            playsound('data\s2.mp3')
            cv2.imshow("image",img)

        if x>320 and x < 460 and y > 190 and y < 310:            
            playsound('data\s1.wav')
            cv2.imshow("image",img)

        if x>50 and x < 190 and y > 190 and y < 310:            
            playsound('data//floor_tom.wav')
            cv2.imshow("image",img)


img = np.ones((512,512,3),dtype = np.uint8)

cv2.rectangle(img,(200,200),(310,310),(255,0,0),-1)
cv2.putText(img, "BASS", (220, 250), font, 1,  (255, 255, 0),  2) 
cv2.rectangle(img,(320,190),(460,310),(255,0,0),-1)
cv2.putText(img, "SNARE", (350, 250), font, 1,  (255, 255, 0),  2) 
cv2.rectangle(img,(50,190),(190,310),(255,0,0),-1)
cv2.putText(img, "TOM", (100, 250), font, 1,  (255, 255, 0),  2) 

#cv2.circle(img,(256,256),50,(255,0,0),-1)
cv2.imshow("image",img)
cv2.setMouseCallback('image', mouse_event) 

cv2.waitKey(0)