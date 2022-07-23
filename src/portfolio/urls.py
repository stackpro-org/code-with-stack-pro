from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    # path('portfolio_api', views.Portfolio_api.as_view(),),
    path('details/<str:slug>/', views.details, name='details'),
    path('api/',include('portfolio_api.urls')),
 
]
