from rest_framework import serializers
from about.models import Testimonial1, Client, About, Count, Testimonial2, Client_image



class About_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id','img','title','text1','text2']


class Client_image_serializer(serializers.ModelSerializer):
    class Meta:
        model = Client_image
        fields = ['id','name','image']

class Client_Serializer(serializers.ModelSerializer):
    client_image =Client_image_serializer(many=True)
    class Meta:
        model = Client
        fields = ['id','title','text','client_image']




class Count_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ['id','number','subtitle','shorttext','url']



class Testimonial1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial1
        fields = ['id','title','subtitle']

class Testimonial2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial2
        fields = ['id','name','img','title','text']

