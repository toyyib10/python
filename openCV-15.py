import cv2
import face_recognition as FR
font = cv2.FONT_HERSHEY_SIMPLEX
width = 640
height = 360
cam = cv2.VideoCapture(4)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

toyFace = FR.load_image_file('/home/owner/work/python/demoImages/known/Toy.jpeg')
faceLoc = FR.face_locations(toyFace)[0]
toyFaceEncode = FR.face_encodings(toyFace)

abdFace = FR.load_image_file('/home/owner/work/python/demoImages/known/Abd.jpeg')
faceLoc = FR.face_locations(abdFace)[0]
abdFaceEncode = FR.face_encodings(abdFace)

knownEncodings = [toyFaceEncode,abdFaceEncode]
names = ['Toyyib', 'Abdullah']
while True:
    ignore, unknownFace = cam.read()
    unknownFaceRGB = cv2.cvtColor(unknownFace,cv2.COLOR_BGR2RGB)
    faceLocations = FR.face_locations(unknownFaceRGB)
    unknownEncodings = FR.face_encodings(unknownFaceRGB, faceLocations)
    for faceLocation, unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left = faceLocation
        cv2.rectangle(unknownFace, (left,top),(right,bottom),(255,0,0),3)
        name = 'Unknown Person'
        # matches = FR.compare_faces(knownEncodings,unknownEncoding)
        # if True in matches:
        #     matchIndex = matches.index(True)
        #     print(matchIndex)
        #     name= names[matchIndex]
        # cv2.putText(unknownFace,name,(left,top),font,.75,(0,0,255),3,2)
    cv2.imshow('My Faces',unknownFace)
    cv2.moveWindow('my Faces',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()