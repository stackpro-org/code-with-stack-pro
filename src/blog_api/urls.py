from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_api.as_view()),
    path('detail/<str:pk>/<str:slug>/', views.Retrive_update.as_view(), name="detail"),
    path('search/',views.Search_api.as_view())

]


