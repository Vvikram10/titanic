from django.urls import path
from . import views

urlpatterns = [
#    path('', views.result, name='result'),
   path('', views.home, name='home'),
   path('result/', views.result, name='result'),
] 