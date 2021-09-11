

from django.db.models import fields, manager
from users.models import last_detected_images
from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
user = get_user_model()  

# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = last_detected_images
#         fields='__all__'
        
        

class FaceDetectedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = last_detected_images
        fields = ('id', 'file','user')
        

