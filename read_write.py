import cv2
import numpy as np 
from matplotlib import pyplot as plt 

cap = cv2.VideoCapture(0)
img = cv2.imread("data\\lena.jpg")
cv2.imshow("img frame",img)
cv2.waitKey(0)
while(cap.isOpened()):
    ret,frame = cap.read()
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break