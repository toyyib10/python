import cv2
import mediapipe as mp
print(cv2.__version__)
width = 1280
height = 640
cam = cv2.VideoCapture(4)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

circleY = int(height/2)
circleX = int(width/2)

deltaX = 3
deltaY = 3
score = 0
hands = mp.solutions.hands.Hands(False, 2, min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils 
while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frameRGB)
    myHands = []
    cv2.circle(frame, (circleX, circleY), 20, (255,0,0),-1)
    if result.multi_hand_landmarks != None:
        for handLandMarks in result.multi_hand_landmarks:
            myHand = []
            mpDraw.draw_landmarks(frame, handLandMarks, mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in handLandMarks.landmark:
                myHand.append((int(landmark.x * width),int(landmark.y * height)))
            myHands.append(myHand)
            cv2.rectangle(frame, ((myHands[0][12][0]-50),0),((myHands[0][12][0]+50),20),(0,255,0),-1)
    circleX= circleX + deltaX
    circleY = circleY + deltaY
    if circleY-20 <= 20:
        if circleX > (myHands[0][12][0]-50) and circleX < (myHands[0][12][0]+50):
            deltaY = (deltaY*-1)
            score = score + 1
        else:
            circleY = int(height/2)
            circleX = int(width/2)
            score = score - 1
    if circleY-20<=0 or circleY >= height:
        deltaY = (deltaY*-1)
    if circleX-20 <= 0 or circleX + 20 >= width:
        deltaX = (deltaX*-1)
    print(score)
    cv2.putText(frame,str(score),(width-160,height-40), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 