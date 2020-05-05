from cv2 import cv2
img = cv2.imread('lena.jpg',1)
cv2.imshow('lena_img',img)
cv2.waitKey(0)
#b,g,r = cv2.split(img)
#print(b,g,r)
#print(img)
#cv2.imwrite('lena_copy.png',img)


img = cv2.resize(img,(255,255))
cv2.imshow('b',img)
cv2.waitKey(0)