import cv2 
import numpy as np
import face_recognition
from users.models import UserAccount
from django.conf import settings
import os 
from PIL import Image
import datetime
from random import randint
import uuid
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth import get_user_model
from users.models import last_detected_images
from icecream import ic
from pprint import pprint
from django.core.files.storage import default_storage
from attendence.models import FaceEncoding

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    print('encoding Complete')
    return encodeList

def findMatch(userImage,Encodings,classNames):
    print('matching')
    imgS = cv2.resize(userImage, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurrentFrame = face_recognition.face_locations(imgS,number_of_times_to_upsample=2)
    encodesCurrentFrame = face_recognition.face_encodings(imgS, facesCurrentFrame)
    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(Encodings, encodeFace)
        faceDis = face_recognition.face_distance(Encodings, encodeFace)
        print(faceDis,'this is the fase distance')
        matchIndex = faceDis.argmin(axis=0)
        print(matchIndex,'this is the match index ---')
        print(type(matches[matchIndex]),'this is the matches')
        if matches[matchIndex]:
            currentTime = datetime.datetime.now()
            name = classNames[matchIndex]
            user = get_user_model()
            user = user.objects.filter(
                profile_pic=f'profile_pic/{name}.png')
 
            return user[0]
        else:
            print('no match found')
        
def hi(userImage=None):

    # userImage = cv2.imread(settings.MEDIA_ROOT+'/' +
    #     UserAccount.objects.values_list('profile_pic', flat=True)[1])
    # Load image as string from file/database
    # print(userImage)
    img = cv2.imdecode(np.fromstring(
        userImage.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    userImage = img
    # images = []
    # classNames = []
    # myList = UserAccount.objects.values_list('profile_pic', flat=True)
    # for  cl in myList:
    #     file = default_storage.open(cl)
    #     readFile = file.read()
    #     file.close()
    #     nparr = np.fromstring(readFile, np.uint8)
    #     img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #     print(len(img_np),'the image is read ---------------')
    #     # curImg = cv2.imread(readFile)
    #     # print(curImg, 'the image is read----------')
    #     images.append(img_np)
    #     classNames.append(os.path.splitext(cl)[0][12:])
    # Encodings=findEncodings(images)
    # print(classNames)
    # print(Encodings)
    # pprint(userImage)
    FaceEncodes = FaceEncoding.objects.all().first()
    Encodings = FaceEncodes.encodings
    # Encodings = np.array(np.array(Encodings))
    # Encodings = [Encodings]
    # print(Encodings, 'from the face detecht-------------------------->>>>> ')
    newEncodings = []
    for i in range(len(Encodings)):
        newEncodings.append(np.array(Encodings[i]))
    print(newEncodings, 'from the face detecht-------------------------->>>>> ')
    classNames = FaceEncodes.classNames
    results = findMatch(userImage, newEncodings, classNames)
    print(results,'results')
    return results