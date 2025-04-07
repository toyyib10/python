import os
import face_recognition as FR
import cv2
names = []
font = cv2.FONT_HERSHEY_SIMPLEX
knownEncodings = []
imageDir = '/home/owner/work/python/demoImages/known'
for root, dirs, files in os.walk(imageDir):
    for file in files:
        filePath = os.path.join(root,file)
        names.append(os.path.splitext(file)[0])
        face = FR.load_image_file(filePath)
        knownEncodings.append(FR.face_encodings(face)[0])
unknownImage = '/home/owner/work/python/demoImages/unknown'

for root, dirs, files in os.walk(unknownImage):
    for file in files:
        filePath = os.path.join(root,file)
        face = FR.load_image_file(filePath)
        unknownFace = cv2.cvtColor(face,cv2.COLOR_RGB2BGR)
        unknownFaceLocs = FR.face_locations(face)
        unknownEncodings = FR.face_encodings(face, unknownFaceLocs)
        for unknownEncoding, unknownFaceLoc in zip(unknownEncodings, unknownFaceLocs):
            top,right,bottom,left = unknownFaceLoc
            cv2.rectangle(unknownFace, (left,top),(right,bottom),(255,0,0),3)
            matches = FR.compare_faces(knownEncodings,unknownEncoding)
            name = 'Unknown Face'
            if True in matches:
                global matchIndex
                matchIndex = matches.index(True)
                name = names[matchIndex]
            cv2.putText(unknownFace,name,(left,(top-10)),font,.75,(0,0,255),3,2)
        cv2.imshow('Faces',unknownFace)
        cv2.resizeWindow('Faces',640,360)
        cv2.waitKey(2000)