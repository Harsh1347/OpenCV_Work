import cv2
import numpy as np

img = cv2.imread("data//opencv.png")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray_img,175,255,0)

contours,hirec = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print("no of countors = "+str(len(contours)))

cv2.drawContours(img,contours,-1,(100,25,55),2)

cv2.imshow("image",img)
cv2.imshow("gray",gray_img)
cv2.waitKey(0)