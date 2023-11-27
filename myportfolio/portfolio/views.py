# portfolio/views.py
from django.shortcuts import render
from .models import Project

def Home(request):
    return render(request,'home.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

