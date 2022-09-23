from django.urls import path

from . import views

urlpatterns = [
            path('login', views.login, name='login'),
            path('logout', views.logout, name='logout'),
            path('', views.dashboard, name='dashboard'),
            path('users', views.profile, name='users'),
            path('drivers', views.Drivers, name='drivers'),
            path('approvers', views.Approvers, name='approvers'),

]