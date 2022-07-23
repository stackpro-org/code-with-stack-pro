from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about_page, name='about'),
    path('api/', include('about_api.urls')),
]