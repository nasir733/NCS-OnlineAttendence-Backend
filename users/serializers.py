from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name',
                  'profile_pic', 'roll_no', 'grade', 'phone_number', 'address')
        # exclude = ('profile_thumbnail' )
        
        
