import cv2
print(cv2.__version__)
import numpy as np
steps= int(input("How many step? "))
size= int(input("How many box? "))
color=(0,0,0)
while True:
    frame=np.zeros([steps,steps,3], dtype=np.uint8)
    for i in range(0,steps):
        for j in range(0,steps):
            frame[(size*i):(size*(i+1)),(size*j):(size*(j+1))] = color
            if (color==(0,0,0)):
                color=(0,0,255)
            else: 
                color=(0,0,0)
        if (color==(0,0,0)):
            color=(0,0,255)
        else: 
            color=(0,0,0)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break