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
    # pprint(imgS)
    facesCurrentFrame = face_recognition.face_locations(imgS,number_of_times_to_upsample=2)
    # pprint(facesCurrentFrame)
    encodesCurrentFrame = face_recognition.face_encodings(imgS, facesCurrentFrame)
    # pprint(encodesCurrentFrame)
    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(Encodings, encodeFace)
        faceDis = face_recognition.face_distance(Encodings, encodeFace)
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            currentTime = datetime.datetime.now()
            name = classNames[matchIndex]
            print(name,'this name is found')
            user = get_user_model()
            user = user.objects.filter(
                profile_pic=f'profile_pic/{name}.png')
            # print(user)
 
            # print(name+'.png')
            # print(user[0], 'found')
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
    images = []
    classNames = []
    myList = UserAccount.objects.values_list('profile_pic', flat=True)
    for  cl in myList:
        curImg = cv2.imread(settings.MEDIA_ROOT+'/'+cl)
        images.append(cv2.imread(settings.MEDIA_ROOT+'/'+cl))
        print()
        classNames.append(os.path.splitext(cl)[0][12:])
    Encodings=findEncodings(images)
    print(classNames)
    # print(Encodings)
    # pprint(userImage)
    results = findMatch(userImage, Encodings, classNames)
    print(results,'results')
    return results

    

