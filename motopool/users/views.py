from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login(request):
   # return redirect('dashboard')
   return render(request, "users/login.html")

def dashboard(request):
    return render(request, "users/dashboard.html")