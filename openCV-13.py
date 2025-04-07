import cv2
print(cv2.__version__)
width = 640
height = 360
cam = cv2.VideoCapture(4)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')

while True:
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        frameFace = frame[y:y+h,x:x+w]
        frameFaceGray = cv2.cvtColor(frameFace,cv2.COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(frameFaceGray,1.3,5)
        for eye in eyes:
            xe,ye,we,he = eye
            cv2.rectangle(frame[y:y+h,x:x+w], (xe,ye),(xe+we,ye+he),(255,0,0),2)
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 