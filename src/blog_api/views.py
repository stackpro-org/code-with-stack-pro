
from rest_framework.decorators import permission_classes
from blog.models import Post
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated, AllowAny, BasePermission, SAFE_METHODS, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView, get_object_or_404
# Create your views here.
from .serializers import Post_serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



#custom permission for edit post. the user write the post will be caught
class PostUserWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user



class Post_api(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Post.objects.all()
    serializer_class = Post_serializer
    filterset_fields = ['headline']
 


class Retrive_update(RetrieveUpdateDestroyAPIView,PostUserWritePermission):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = Post_serializer
    authentication_classes = [  
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
        ]


class Search_api(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Post_serializer

    
    def get_queryset(self, *args, **kwargs):

        #here get_queryset is inheritate from another class by super()
        qs = super().get_queryset(*args,**kwargs)

        # here took the params from url
        q = self.request.GET.get('q')
        result = Post.objects.none()
        if q is not None:

            #here we sent the params to the finding method in medels
            result = qs.finding(q)
        return result



  


