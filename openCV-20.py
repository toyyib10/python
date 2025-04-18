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
findFace = mp.solutions.face_detection.FaceDetection()
drawFace = mp.solutions.drawing_utils

while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = findFace.process(frame)
    if result.detections != None:
        for face in result.detections:
            # drawFace.draw_detection(frame,face)
            bBox=face.location_data.relative_bounding_box;
            pt1 = (int(bBox.xmin * width),int(bBox.ymin * height))
            pt2 = (int((bBox.xmin + bBox.width) * width),int((bBox.ymin + bBox.height) * height))
            cv2.rectangle(frame,pt1,pt2,(125,125,0), 2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()