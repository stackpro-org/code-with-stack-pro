from rest_framework import serializers

from django.contrib.auth.models import User


# class Profile_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

from . models import Profile
from django.contrib.auth.models import User

class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

