import cv2
print(cv2.__version__)
import numpy as np

frame = np.zeros([800,800,3],dtype=np.uint8)

while True:
    numC=(0,0,0)
    for i in range(0,10):
        for j in range(0,10):
            frame[80*i:80*(i+1),80*j:80*(j+1)]=numC
            if numC == (0,0,0):
                numC=(0,0,255)
            else:
                numC=(0,0,0)
        if numC == (0,0,0):
            numC=(0,0,255)
        else:
            numC=(0,0,0)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break