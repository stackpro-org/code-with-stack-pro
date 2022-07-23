from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.Service_view.as_view()),
    path('skill/',views.Skill_view.as_view()),
]