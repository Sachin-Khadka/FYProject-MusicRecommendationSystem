from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError


def Admin_Dashboard(request):
    return render(request, 'user-dashboard.html')

def User_Dashboard(request):
    return render(request, 'admin-dashboard.html')    