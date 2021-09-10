from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from .face_detect import hi
# Create your views here.
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework import authentication, permissions 

class detect_face(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    def post(self,request,*args,**kwargs):
        picture = request.FILES.get('picture')
        print(request.FILES.get('picture'))
        hi(userImage=picture)
        # return response(status=200)
        return HttpResponse("Hello, world. You're at the detect_face index.")
