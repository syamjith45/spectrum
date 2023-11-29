

# Create your views here.
from django.shortcuts import render, redirect
from .forms import Userform
def create_user(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Userform()

    return render(request, 'forms.html' ,{'form': form })

