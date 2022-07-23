from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.services, name='services'),
    path('api/', include('service_api.urls')),
  
]