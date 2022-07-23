from rest_framework.views import APIView
from rest_framework import generics
from .serializers import Service_serializer, Skill_serializer
from services.models import Service, Skill
from rest_framework.response import Response

class Service_view(APIView):
    def get(self,request,*args, **kwargs):
        service = Service.objects.all()

        service_serializer = Service_serializer(service, many=True)

        return Response(service_serializer.data)



class Skill_view(generics.ListAPIView):

    queryset = Skill.objects.all()

    serializer_class = Skill_serializer
