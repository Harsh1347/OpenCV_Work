import cv2
import numpy as np 
import tensorflow as tf 

model = tf.keras.models.load_model('side//gest.h5')
CATEGORIES = ['peace','thumbup','okay']
cap = cv2.VideoCapture(0)
i=100
while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.rectangle(frame,(0,0),(300,300),(0,0,255),2)
    roi = frame[0:300,0:300]

    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(roi,155,255,cv2.THRESH_BINARY_INV)
    blur = cv2.GaussianBlur(thresh,(3,3),0)

    dilate = cv2.dilate(blur,None,iterations=3)
    erode = cv2.erode(dilate,None,iterations=3)

    contours , _ = cv2.findContours(erode,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(255,0,0),3)

    img = cv2.resize(erode,(50,50))
    x = np.array(img).reshape(-1,50,50,1)
    pred = model.predict(x)
    pred = CATEGORIES[np.argmax(pred)]
    if pred in CATEGORIES:
        
        cv2.putText(frame,pred,(150,400),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),1)
    else:
        cv2.putText(frame,"Waiting",(150,400),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),1)
    cv2.imshow('roi',roi)
    cv2.imshow("dilate first",erode)
    cv2.imshow("frame",frame)
    #print(erode.shape)
    # if cv2.waitKey(1) & 0xFF == ord('c'):
    #     cv2.imwrite(f'img//thumbup//{i}.png', erode)
    #     i-=1
    #     if i < 0:
    #         break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cap.release()
cv2.destroyAllWindows()