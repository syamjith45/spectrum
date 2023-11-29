from django.urls import path
from .views import create_user
urlpatterns = [
    path('forms/', create_user, name='create_user'),
# Add other URLs as needed
]