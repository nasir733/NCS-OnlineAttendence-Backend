
from django.http.response import HttpResponse
from django.shortcuts import render
from .face_detect import hi
from .models import Attendence
# Create your views here.
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework import authentication, permissions 
from rest_framework.response import Response
from .serializers import FaceDetectedSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from icecream import ic
from users.models import UserAccount
class detect_face(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    def post(self,request,*args,**kwargs):
        picture = request.FILES.get('picture')
        print(request.data)
        detect = hi(userImage=picture)
        serializer = FaceDetectedSerializer(detect)
        print(serializer)
        return Response(serializer.data, status=HTTP_200_OK)
       
        
class attendence(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    def post(self,request,*args,**kwargs):
        print(request.data)
        year = request.data.get('year')
        month = request.data.get('month')
        day = request.data.get('day')
        time = request.data.get('time')
        user = request.data.get('user')
       
        # try:
        attendece= Attendence.objects.get_or_create(year=year,month=month,day=day)
        print(user)
        print(attendece[0].presentStudents)
        userObject = UserAccount.objects.get(id=user)
        if userObject in attendece[0].presentStudents.all():
            return Response({"message":"Already Present"})
        attendece[0].presentStudents.add(user)
        return Response(status=HTTP_200_OK)
        # except:
        #     return Response(status=HTTP_400_BAD_REQUEST)
