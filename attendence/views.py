from django.http.response import HttpResponse
from django.shortcuts import render
from .face_detect import hi
# Create your views here.
def detect_face(request):
    hi()
    return HttpResponse("Hello, world. You're at the detect_face index.")