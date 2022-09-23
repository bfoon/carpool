from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
# from .models import Profile
from myapp.models import Profile, Vehicle
from django.db import connections
from django.contrib.auth.decorators import login_required
# Create your views here.
def vehicle_list(request):
    vehicle = Vehicle.objects.all()
    context = {
        "vehicle":vehicle
    }
    return render(request, "vehicles/vehicles-table.html", context)