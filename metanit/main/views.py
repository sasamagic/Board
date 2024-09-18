from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from database.models import Modules
from .forms import regForm

# Create your views here.

def index(request):
    return render(request,'main/index.html')
def user (request):
    return render(request,'main/user.html')
def modules (request):
    error = ''
    if request.method == 'POST':
        form = regForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status')
        else:
            error = 'ахтунг ошибка'
    else:
        form = regForm()  # Create an empty form for GET requests

    context = {
        'form': form,
        'error': error
    }
    return render(request,'main/modules.html',context) # пока работаю с этой фигней#
def status (request):
    product = Modules.objects.all()
    context = {
        'pr': product
    }
    return render(request,'main/status.html',context)

def logout_view(request):
    auth_logout(request)
    return redirect('home')
def registration (request):
    return render(request,'main/registration.html')