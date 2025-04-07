import cv2
print(cv2.__version__)
width = 640
height = 360
xPos=0
yPos=0
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

def callBack(value):
    global width
    width=value

def callBackY(value):
    global height
    height = value

def callBackM(value):
    global xPos
    xPos=value

def callBackMY(value):
    global yPos
    yPos = value

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',400,150)
cv2.moveWindow("Trackbars",width+100,0)
cv2.createTrackbar('xPos','Trackbars', width, 16000, callBack)
cv2.createTrackbar('yPos','Trackbars', height, 9000, callBackY)
cv2.createTrackbar('xPos1','Trackbars', xPos, 1600, callBackM)
cv2.createTrackbar('yPos1','Trackbars', yPos, 900, callBackMY)

while True:
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    ignore, frame = cam.read()
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow('my WEBcam',xPos,yPos)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 