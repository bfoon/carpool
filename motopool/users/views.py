from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
   # return redirect('dashboard')
   # return render(request, "users/login.html")


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request, "users/dashboard.html")

@login_required(login_url='login')
def users(request):
    return render(request, "users/users-table.html")