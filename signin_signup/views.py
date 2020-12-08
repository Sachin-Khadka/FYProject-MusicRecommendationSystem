from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.

def registrationForm(request):
    return render(request,'Register.html')
    

# This is manual process. 
# def registration_form_save(request):
#     if request.method == "GET":
#         return render(request,'Login.html')
#     else:
#         try:
#             user = User.objects.create_user(username=request.POST['username'],first_name= request.POST['first_name'], last_name = request.POST['last_name'],
#             email=request.POST['email'],password= request.POST['password'])
#             user.save()    
#             messages.info(request, "Account Successfully Created. You can Sign In.")
#             return redirect('login')

#         except IntegrityError:
#             messages.error(request,"A user with that username already exists")
#             return redirect('register')


# def loginForm(request):
#     return render(request,'Login.html')

def Login_auth(request):
    if request.method == "GET":
        return render(request,'Login.html')
    else:
        auth_user = authenticate(username=request.POST['authusername'], password=request.POST['authpassword'])   
        if auth_user is not None:
            login(request, auth_user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
            
def logoutSession(request):
    logout(request)
    return redirect('/')
        

# This is first method
def registrationPage(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login.')
            return redirect('login')
            
    else:   
        # form = UserCreationForm()
        form = UserRegistrationForm()
    return render(request, 'Register.html', {'form':form})



# This is Second method 
# def registrationPage(request):
#     form =  UserRegistrationForm()
    
#     if request.method=='POST':
#         form = UserRegistrationForm()
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'Register.html', context)

 