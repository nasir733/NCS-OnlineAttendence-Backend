from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.detect_face,name="detect_face"),
]
