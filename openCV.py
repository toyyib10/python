import cv2
print(cv2.__version__)
width = 320
height = 180
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,frame = cam.read()
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow('my WEBcam',0,0)
    cv2.imshow("myWEBcam", frame)
    cv2.moveWindow('myWEBcam',190,0)
    cv2.imshow("mWEBcam", frame)
    cv2.moveWindow('mWEBcam',290,0)
    cv2.imshow("WEBcam", frame)
    cv2.moveWindow('WEBcam',390,0)
    cv2.imshow("my WEBam", frame)
    cv2.moveWindow('my WEBam',490,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 