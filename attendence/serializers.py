

from django.db.models import fields, manager
from users.models import last_detected_images
from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
user = get_user_model()  
from .models import Attendence

# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = last_detected_images
#         fields='__all__'
        
        
 
class attendnetuserSeializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','first_name','last_name','email')       
class AttendenceSerializer(serializers.ModelSerializer):
    presentStudents = attendnetuserSeializer(many=True)
    class Meta:
        model = Attendence
        fields = ('year', 'month', 'day', 'time', 'presentStudents')

class FaceDetectedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    file = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = last_detected_images
        fields = ('id', 'file','user')
    def get_image_url(self, obj):
        return obj.file.url

