from rest_framework import generics
from about.models import About, Client, Count, Testimonial2, Testimonial1
from . serializers import About_Serializer,Client_Serializer, Count_Serializer, Testimonial2_Serializer, Testimonial1_Serializer


class About_View(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = About_Serializer


class Client_View(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = Client_Serializer



class Count_View(generics.ListAPIView):
    queryset = Count.objects.all()
    serializer_class = Count_Serializer
 
 
class Testimonial1_View(generics.ListAPIView):
    queryset = Testimonial1.objects.all()
    serializer_class = Testimonial1_Serializer



class Testimonial2_View(generics.ListAPIView):
    queryset = Testimonial2.objects.all()
    serializer_class = Testimonial2_Serializer