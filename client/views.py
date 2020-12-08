from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def client_home(request):
    return render(request, "client-home-page.html")


