from django.urls import path
from .views import *
urlpatterns = [
    path('client/', client_home, name='client-home'),

]


