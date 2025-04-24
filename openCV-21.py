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

class pose:
    def __init__(self, still = False, num = 1, upper = True):
        import mediapipe as mp
        self.pose = mp.solutions.pose.Pose(still,num, upper, False, True, .5, .5)
    def Marks(self, frame):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(frameRGB)
        mark = []
        for lm in result.pose_landmarks.landmark:
            mark.append((int(lm.x * width),int(lm.y * height)))
        return mark
poseDetect = pose()

while True:
    ignore, frame = cam.read()
    result = poseDetect.Marks(frame)
    print(result)
    for pt in result:
        cv2.circle(frame, pt, 25, (125,0,125), 1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 