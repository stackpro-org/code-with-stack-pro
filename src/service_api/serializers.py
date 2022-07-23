from rest_framework import serializers
from services.models import Service, Skill


class Service_serializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'



class Skill_serializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
