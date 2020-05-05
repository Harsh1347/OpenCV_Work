from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#time.sleep(3)
background=0
for i in range(30):
    ret,background = cap.read()
    cv2.imshow("video", background)
    key = cv2.waitKey(1)
    if key == 27:
        break
print(background,"done")

# Capturing the live frame
while(True):
    ret, img = cap.read()

    # converting from BGR to HSV color space
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Range for lower red
    lower_red = np.array([0,140,90])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Range for upper range
    lower_red = np.array([170,140,90])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)


    # Generating the final mask to detect red color
    mask = mask1+mask2
    #print("mask created")

    mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))


    #creating an inverted mask to segment out the cloth from the frame
    mask2 = cv2.bitwise_not(mask1)


    #Segmenting the cloth out of the frame using bitwise and with the inverted mask
    res1 = cv2.bitwise_and(img,img,mask=mask2)

    # creating image showing static background frame pixels only for the masked region
    res2 = cv2.bitwise_and(background, background, mask = mask1)


    #Generating the final output
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("magic",final_output)
    key = cv2.waitKey(1)
    if key == 27:
        break
