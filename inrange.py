import cv2 as cv
import numpy as np
fourcc=cv.VideoWriter_fourcc(*'XVID')


cap=cv.VideoCapture(0)
width=cap.get(3)
height=cap.get(4)
size=(width,height)
result=cv.VideoWriter('output.avi',fourcc,20,(640,480))
for i in range(30):
    ret,background=cap.read()
while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  
    l_b=np.array([0,120,70])
    u_b=np.array([10,255,255])
    mask1=cv.inRange(hsv,l_b,u_b)
    l_b=np.array([170,120,70])
    u_b=np.array([180,255,255])
    mask2=cv.inRange(hsv,l_b,u_b)
    mask1=mask1+mask2
    mask1=cv.morphologyEx(mask1,cv.MORPH_OPEN,np.ones((2,2),dtype='uint8'),iterations=2)
    mask1=cv.morphologyEx(mask1,cv.MORPH_DILATE,np.ones((2,2),dtype='uint8'),iterations=1)
    mask2=cv.bitwise_not(mask1)
    res1=cv.bitwise_and(background,background,mask=mask1)
    res2=cv.bitwise_and(img,img,mask=mask2)
    output_frame=cv.addWeighted(res1,1,res2,1,0)
    result.write(output_frame)
    cv.imshow('croma',output_frame)
    k=cv.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv.destroyAllWindows()

    



