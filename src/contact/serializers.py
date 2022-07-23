from rest_framework import serializers
from .models import  Contact




class Contact_serializer(serializers.ModelSerializer):
    class Meta:
        model =  Contact
        fields = '__all__'

# class Contact_serializer(serializers.ModelSerializer):
#     class Meta:
#         model =  Contact
#         fields = '__all__'

