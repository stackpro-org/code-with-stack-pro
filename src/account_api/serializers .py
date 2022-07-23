from rest_framework import serializers
from account.models import Profile
from django.contrib.auth.models import User



class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

