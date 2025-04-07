import cv2
import numpy as np
print(cv2.__version__)
width = 720
height = 255
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
hue = 720
sat = 255
val = 255

while True:
    ignore, frame = cam.read()
    frame = np.zeros((height,width,3), dtype=np.uint8)
    for i in range(0,sat):
        for j in range(0,hue):
            frame[i,j] = (int(j/4),i,255)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow('my WEBcam',0,0)

    for i in range(0,val):
        for j in range(0,hue):
            frame[i,j] = (int(j/4),255,i)

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    cv2.imshow("my WEB", frame)
    cv2.moveWindow('my WEB',width+100,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 