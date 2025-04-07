import cv2
print(cv2.__version__)
width = 640
height = 360
snipW = 120
snipH = 60
boxCC = int(height/2)
boxCR = int(width/2)

deltaRow = 1
deltaColumn = 1

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
 
while True:
    ignore, frame = cam.read()
    frameROI = frame[(boxCR-int(snipH/2)): (boxCR+ int(snipH/2)), (boxCC-int(snipW/2)):(boxCC + int(snipW/2))]
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR )
    frame[boxCR-int(snipH/2): boxCR+ int(snipH/2), boxCC-int(snipW/2):boxCC + int(snipW/2)] = frameROI
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow('my WEBcam',0,0)
    cv2.imshow("frame Roi", frameROI)
    cv2.moveWindow("frame Roi",700,0 )

    boxCC= boxCC + deltaColumn
    boxCR = boxCR + deltaRow
    if boxCR-int(snipH/2) <= 0 or boxCR+ int(snipH/2) >= height:
        deltaRow = (deltaRow*-1)
    if boxCC-int(snipW/2) <= 0 or boxCC + int(snipW/2) >= width:
        deltaColumn = (deltaColumn*-1)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 