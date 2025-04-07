import cv2
print(cv2.__version__)
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("my WEBcam")
evt=0
pos2 = 0

def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global pos1
    global pos2
    global xPos1 
    global xPos2
    global yPos1
    global yPos2
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        pos1= (xPos, yPos)
        xPos1 = xPos
        yPos1 = yPos

    if event == cv2.EVENT_LBUTTONUP:
        evt = event
        pos2 = (xPos, yPos)
        xPos2 = xPos
        yPos2 = yPos

    if event == cv2.EVENT_RBUTTONUP:
        print(event)
        pos2=0
        pos1=0

cv2.setMouseCallback("my WEBcam", mouseClick)
 
while True:
    ignore, frame = cam.read()
    if evt == 4:
        if pos1 != 0 and pos2 != 0:
            cv2.rectangle(frame, pos1, pos2, (0,255,0), 2)
            frameROI = frame[yPos1:yPos2,xPos1:xPos2]
            cv2.imshow("my WEcam", frameROI)
            cv2.moveWindow('my WEcam',700,0)
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 