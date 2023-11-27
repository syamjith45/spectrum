# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('home/',views.Home, name='home')
]
