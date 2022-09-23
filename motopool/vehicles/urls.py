from django.urls import path

from . import views

urlpatterns = [
            path('vehicle_list', views.vehicle_list, name='vehicle_list'),


]