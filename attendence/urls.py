from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.detect_face.as_view(),name="detect_face"),
    path("attendence/",views.attendence.as_view(),name="attendence"),
    path('see_all_attendence', views.ViewAttendence.as_view(),
         name="see_all_attendence"),
]
