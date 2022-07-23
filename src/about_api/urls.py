from django.urls import path
from . import views

urlpatterns = [
    path('', views.About_View.as_view()),
    path('client/', views.Client_View.as_view()),
    path('count/', views.Count_View.as_view()),
    path('testimonial1/', views.Testimonial1_View.as_view()),
    path('testimonial2/', views.Testimonial2_View.as_view()),
    
]
