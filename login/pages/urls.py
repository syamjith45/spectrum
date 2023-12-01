from django.urls import path
from .import views
from .views import Mytemplateview

urlpatterns = [
    
    path('home/',views.home,name='home'),
    path('my_template/', Mytemplateview.as_view(),name='templateview')

]
