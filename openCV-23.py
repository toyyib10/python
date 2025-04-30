import cv2
print(cv2.__version__)
import numpy as np

tol = 1500
numGest = int(input("Enter the number of gestures: "))
traincnt = 0
gestNames = []
knownGestures = []

for i in range(0,numGest):
    prompt = input(f"Enter the name of the gesture {i+1}: ")
    gestNames.append(prompt)

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=maxHands,
            min_detection_confidence=tol1,
            min_tracking_confidence=tol2
        )
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands


width=1280
height=720
cam=cv2.VideoCapture(4)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands()

keyPoints=[0,4,5,8,9,12,13,16,17,20]
train = True

def findDistance(handData):
    if handData != []:
        distMatrix = np.zeros([len(handData),len(handData)],dtype=float)
        for row in range(0,len(handData)):
            for col in range(0,len(handData)):
                    x = handData[row][0]-handData[col][0]
                    y = handData[row][1]-handData[col][1]
                    distMatrix[row][col] = (x**2+y**2)**(1./2.)
        return distMatrix
def findError(gestureMatrix, unknownMatrix, keyPoints):
    error = 0
    for row in keyPoints:
        for col in keyPoints:
           error = error + abs(gestureMatrix[row][col]-unknownMatrix[row][col])
    return error

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    for i in keyPoints:
        if handData != []:
            cv2.circle(frame,(handData[0][i][0],handData[0][i][1]),25,(155,0,0),2)
        if train == True:
            if handData != []:
                print("Show your Gesture: Press t when you're ready")
                if cv2.waitKey(1) & 0xff == ord('t'):
                    knownGesture = findDistance(handData[0])
                    knownGestures.append(knownGesture)
                    if traincnt >= numGest:
                        print("Training complete")
                        train = False
                    traincnt = traincnt + 1
        else:
            if handData != []:
                for i in range(0,numGest):
                    unknownGesture = findDistance(handData[0])
                    error = findError(knownGestures[i],unknownGesture,keyPoints)
                    if error < tol:
                        cv2.putText(frame,gestNames[i],(0,50),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3)
                        cv2.rectangle(frame,(0,0),(width,height),(0,255,0),-1)
                        break
                    else:
                        cv2.rectangle(frame,(0,0),(width,height),(255,0,0),-1)
                cv2.putText(frame,str(int(error)),(0,100),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()