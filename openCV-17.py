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

hands = mp.solutions.hands.Hands(False, 2, min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
myHand =  [] 
while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frameRGB)
    if result.multi_hand_landmarks != None:
        for handLandMarks in result.multi_hand_landmarks:
            # mpDraw.draw_landmarks(frame, handLandMarks, mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in handLandMarks.landmark:
                cv2.circle(frame,(int(landmark.x * width),int(landmark.y * height)),5,(255,0,0), -1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 