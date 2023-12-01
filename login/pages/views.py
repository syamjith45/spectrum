from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required
def home(request):
    return render(request,'pages/home.html')
class Mytemplateview(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
    