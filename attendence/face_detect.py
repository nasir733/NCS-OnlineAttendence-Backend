import cv2 
import numpy as np
import face_recognition
from users.models import UserAccount
from django.conf import settings
import os 
path = 'ImagesAttendance'


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    print('encoding Complete')
    return encodeList

def findMatch(userImage,Encodings,classNames):
    imgS = cv2.resize(userImage, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurrentFrame = face_recognition.face_locations(imgS)
    encodesCurrentFrame = face_recognition.face_encodings(imgS, facesCurrentFrame)
    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(Encodings, encodeFace)
        faceDis = face_recognition.face_distance(Encodings, encodeFace)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:


            name = classNames[matchIndex]
#print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(userImage, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(userImage, (x1, y2-35), (x2, y2),
                          (0, 255, 0), cv2.FILLED)
            cv2.putText(userImage, name, (x1+6, y2-6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            user = UserAccount.objects.filter(
                profile_pic=name+'.jpg')
            print(name+'.jpg')
            print(user, 'found')

        
def hi(userImage=None):
    userImage = cv2.imread(settings.MEDIA_ROOT+'/' +
        UserAccount.objects.values_list('profile_pic', flat=True)[1])
    images = []
    classNames = []
    myList = UserAccount.objects.values_list('profile_pic', flat=True)
    for  cl in myList:
        curImg = cv2.imread(settings.MEDIA_ROOT+'/'+cl)
        images.append(cv2.imread(settings.MEDIA_ROOT+'/'+cl))
        print()
        classNames.append(os.path.splitext(cl)[0][12:-1])
    print(classNames)
    Encodings=findEncodings(images)
    findMatch(userImage, Encodings, classNames)
    

