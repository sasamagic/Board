from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
# Create your views here.

def index(request):
    return render(request,'main/index.html')
def user (request):
    return render(request,'main/user.html')
def modules (request):
    return render(request,'main/modules.html')
def status (request):
    return render(request,'main/status.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')