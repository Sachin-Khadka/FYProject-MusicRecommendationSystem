from django.urls import path
from .views import *

urlpatterns = [
    path('adminDashboard/', Admin_Dashboard, name='admin-dashboard'),
    path('userDashboard/', User_Dashboard, name='user-dashboard'),   
]