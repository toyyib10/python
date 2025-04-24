import cv2
import mediapipe as mp
print(cv2.__version__)
width = 1280
height = 640
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

class faceMesh:
    def __init__(self, still = False, num = 3):
        import mediapipe as mp
        self.faceMesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=False,max_num_faces=3,min_detection_confidence=0.5,min_tracking_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils
    def Marks(self, frame):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(frameRGB)
        if results.multi_face_landmarks != None:
            for faceLandmarks in results.multi_face_landmarks:
                drawing_spec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)
                self.mpDraw.draw_landmarks(frame, faceLandmarks, mp.solutions.face_mesh.FACEMESH_CONTOURS, drawing_spec, drawing_spec)
face_mesh = faceMesh()

while True:
    ignore, frame = cam.read()
    face_mesh.Marks(frame)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release() 