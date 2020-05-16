from cv2 import cv2
face_cascade = cv2.CascadeClassifier('data//haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.5,minNeighbors = 5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        color = (255,0,0) #BGR
        stroke = 2
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke )

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"Face Detection",(15,25),font ,1,color = (255,0,0),thickness=1)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

