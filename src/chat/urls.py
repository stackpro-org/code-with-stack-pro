from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    
    path('', views.chat, name='chat'),
   
    path('friend_list/', views.friend_list, name='friend_list'),

    path('<str:room_name>/', views.room, name='room'),

    path('personal/<str:id>/', views.personal_chat, name='personal_chat'),

    
]
