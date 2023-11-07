from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def print_hello(request):
#     return HttpResponse("<b>Hello world</b>")

def print_hello(request):
    sat_score={
        'sat':[{'name':'syam'
               ,'age':23,
               'course':'python',
               'marks':5,
               'status':False},
               {'name':'Bony'
               ,'age':23,
               'marks':45,
               'status':True},
               {'name':'Arjun'
               ,'age':23,
               'course':'c',
               'marks':45,
               'status':True},
               {'name':'vishu'
               ,'age':23,
               'course':'c++',
               'marks':45,
               'status':True},
               {'name':'Roshan'
               ,'age':23,
               'course':'Java',
               'marks':45,
               'status':True}

        ]

    }
    return render(request,'index.html',sat_score)

