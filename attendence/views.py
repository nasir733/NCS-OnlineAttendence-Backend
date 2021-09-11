
from django.http.response import HttpResponse
from django.shortcuts import render
from .face_detect import hi
# Create your views here.
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework import authentication, permissions 
from rest_framework.response import Response
from .serializers import FaceDetectedSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
class detect_face(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    def post(self,request,*args,**kwargs):
        picture = request.FILES.get('picture')
        print(request.FILES.get('picture'))
        detect = hi(userImage=picture)
        serializer = FaceDetectedSerializer(detect)
        print(serializer)
        return Response(serializer.data, status=HTTP_200_OK)
       
        
