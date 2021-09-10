from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def detect_face(request):
    return HttpResponse("Hello, world. You're at the detect_face index.")