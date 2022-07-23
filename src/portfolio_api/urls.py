from django.urls import path
from . import views
urlpatterns = [
    path('', views.List.as_view()),
    path('retrive/<str:pk>/<str:title>/',views.Retrive.as_view(), name='retrive'),
    path('category/',views.Category.as_view(), name='category'),

]
