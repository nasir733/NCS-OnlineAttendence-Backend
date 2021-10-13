
from django.core.files.storage import default_storage
from attendence.models import FaceEncoding
import cv2
import numpy as np
import face_recognition
from django.contrib.auth import get_user_model
import os
import json
from core.celery import app
from pprint import pprint
from celery import shared_task
from users.models import UserAccount
User = get_user_model()


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    print('encoding Complete')
    return encodeList


def hello(sender, instance, created, *args, **kwargs):
    if created:
        print('the model is saved ======================')


@shared_task()
def MakeFaceEncoding(*args, **kwargs):
    print('MakeFaceEncoding Reciever is runing------')
    images = []
    classNames = []
    myList = UserAccount.objects.values_list('profile_pic', flat=True)
    for cl in myList:
        file = default_storage.open(cl)
        readFile = file.read()
        file.close()
        nparr = np.fromstring(readFile, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print(len(img_np), 'the image is read ---------------')
        # curImg = cv2.imread(readFile)
        # print(curImg, 'the image is read----------')
        images.append(img_np)
        classNames.append(os.path.splitext(cl)[0][12:])
    print('hello my friend')

    Encodings = findEncodings(images)
    newEncodings = []
    # print(len(Encodings),'the length of encodings is ---------- ---===>>>')
    for i in range(len(Encodings)):
        print(type(Encodings[i]))
        newEncodings.append(Encodings[i].tolist())
        # print(newEncodings,'these are new incodings -------------======')
    print(type(newEncodings), 'the length of encodings is ----------')
    FaceEncodings = FaceEncoding.objects.all().update(
        encodings=newEncodings, classNames=classNames)
