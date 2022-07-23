from django.urls import path
from . import views
urlpatterns = [
    path('', views.team, name='team'),


        #API path
    path('api/',views.Team_api.as_view()),
    path('pdf/',views.GeneratePdf.as_view(), name="pdf"),
    

]