import cv2
print(cv2.__version__)
width = 640
height = 360
mRadius=30
color= (0,0,0)
thick=2
myText="Nafeesah"
cam = cv2.VideoCapture(0,)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
f=0
while True:
    ignore,frame = cam.read()
    f = f+1
    frame[140:220,250:390]= (255,0,0)
    cv2.rectangle(frame,(250,140),(390,220),(0,255,0),4)
    cv2.circle(frame,(int(width/2),int(height/2)),mRadius,color,thick)
    cv2.putText(frame,myText,(120,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 