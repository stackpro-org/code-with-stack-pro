from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 

## JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('create/',views.Account_api.as_view(),),
    path('',views.Login_api.as_view(),),
    path('logout/',views.Logout_api.as_view(),),
    
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/',obtain_auth_token),

]
