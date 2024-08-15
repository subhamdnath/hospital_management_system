from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from .models import MyUser
from hospital.models import *


@csrf_exempt
def login_user(request):
    error_message = None
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")
        if not MyUser.objects.filter(email=email).exists():
            messages.error(request, "Error: Email not exits!")
            return redirect("login_user")            
        user = authenticate(request, email=email, password=password)
        if user != None:
            login(request, user)   
            return redirect("home") 
        else:
            messages.error(request, "Error: Email or password is wrong!")
            return redirect("login_user")
    return render(request, "registration/login.html")
        
        
@csrf_exempt
def signup(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        blood_group = request.POST.get("blood_group")
        location = request.POST.get("location")
        marital_status = request.POST.get("marital_status")
        role = request.POST.get("role")

        if MyUser.objects.filter(email=email).exists():
            messages.error(request, "Error: Account with thie email already exits!")
            return redirect("signup")    
        if len(password) < 6:
            messages.error(request, "Error: Password atleast should have 6 characters!")
            return redirect("signup")    
        if name and email and phone_number and password and gender and date_of_birth and blood_group and location and marital_status and role:
            
            user = MyUser.objects.create(name = name, email =email, phone_number = phone_number,
                          password = password, gender = gender, date_of_birth = date_of_birth,
                          blood_group = blood_group, location = location,
                            marital_status = marital_status, role = role )
            user.set_password(password)
            user.save()
            messages.success(request, "Account created successfully! Please login to continue.")
            return redirect ("login_user")
        
    return render(request, "registration/signup.html", context = {"page" : "Signup"})

@csrf_exempt       
@login_required
def change_password(request):
    if request.method == "POST":

        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        if new_password != confirm_password: 
            messages.error(request, "Error: Password doesn't match!")
        else:
            user = request.user        
            if not user.check_password(old_password):
                messages.error(request, "Error: Old password is wrong!")           
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully!")
               
    return render(request, "registration/change_password.html")


@csrf_exempt
def home(request):

    user = request.user
    patient = PatientProfile.objects.get(patient = user)   
    context = {"emergency_contact" : patient.emergency_contact}
    print( patient.emergency_contact)
    
    return render(request, "hospital/home.html", context)


def logout_user(request):
    user=request.user
    print(user)
    logout(request)
    return redirect("login_user")







