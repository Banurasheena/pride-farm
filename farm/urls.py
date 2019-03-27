from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('farmer_detail/', views.farmer_detail, name='farmer_detail'),
    path('officers/', views.officers, name='officers'),
]
