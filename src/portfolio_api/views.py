from rest_framework import generics
from portfolio.models import Portfolio, Category
from .serializers import  Portfolio_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated, AllowAny, BasePermission, SAFE_METHODS, DjangoModelPermissions, IsAuthenticatedOrReadOnly


class List(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = Portfolio_serializer
    permission_classes = [IsAdminUser]
    authentication_classes = [  
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
        ]


class Retrive(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = Portfolio_serializer
    lookup_fields = ["title", "pk"]

class Category(APIView):

    def get(self, request, formant=None):

        '''
        site url/portfolio/api/category/?category=app     (at last app means the category name)
        '''
        # category = request.GET['category']
        category = request.query_params.get('category')

        queryset = Portfolio.objects.filter(catagory__name = category)

        # BY context={'request': request} we sent context to Portfolio_serializer
        serializers = Portfolio_serializer(queryset, many=True, context={'request': request})

        return Response(serializers.data)





    

        
