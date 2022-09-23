from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
# from .models import Profile
from myapp.models import Profile
from django.db import connections
from django.contrib.auth.decorators import login_required

# Get the data from directly from the database server
# cursor = connections['default'].cursor()
# cursor.execute("SELECT...")
# cursor.fetchall()

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
def profile(request):
    usr = Profile.objects.all().order_by("fname")
    context = {
        'usr': usr,
    }
    return render(request, "users/users-table.html", context)

@login_required(login_url='login')
def Drivers(request):
    dvr = Profile.objects.filter(role="Driver").order_by("fname")
    context = {
        'driver': dvr,
    }
    return render(request, "users/drivers-table.html", context)

@login_required(login_url='login')
def Approvers(request):
    appr = Profile.objects.filter(role="Approver").order_by("fname")
    context = {
        'approver': appr,
    }
    return render(request, "users/approver-table.html", context)