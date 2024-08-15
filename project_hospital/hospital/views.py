from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from .views import *
from .models import *

@csrf_exempt
def complete_profile(request):
    if request.method == "POST":

        pp =  PatientProfile.objects.get(patient=request.user) 
        emergency_contact = request.POST.get("emergency_contact")
        id_patient = request.user.id
        user = MyUser.objects.get(id = id_patient)
        pp =  PatientProfile.objects.get(patient=request.user)
        if emergency_contact:
            pp.emergency_contact = emergency_contact
            pp.save()   

        messages.success(request, "Profile updated successfully")
        return redirect('home')
    return render(request, "hospital/complete_profile.html")
    
    
@csrf_exempt
def get_profile(request): 

    user = request.user
    print(user.id)
    return render(request, "hospital/get_profile.html")


@csrf_exempt
def doctor_profile(request):
    if request.method == "POST":

        id_doctor = request.POST.get("doctor")
        experience = request.POST.get("experience")
        specialization = request.POST.get("specialization")
        doctor_fee = request.POST.get("doctor_fee")
        language = request.POST.get("language")
        available_timings = request.POST.get("available_timings")

        if MyUser.objects.filter(id = id_doctor).exists():
            doctor_object = MyUser.objects.get(id=id_doctor)
            
            user = DoctorProfile.objects.create(doctor=doctor_object, experience=experience, specialization=specialization,
                                            doctor_fee=doctor_fee, language=language,
                                            available_timings=available_timings)
        
    return render(request, "hospital/doctor_profile.html")
                

@csrf_exempt
def get_doctor_profile(request):
    if request.method == "POST":

        user = request.user
        print(user)
    return render(request, "hospital/get_doctor_profile.html")


@csrf_exempt
def admin_profile(request):
    if request.method == "POST":

        admin = request.POST.get("admin")
        if MyUser.objects.filter(id = admin).exists():
            admin_object = MyUser.objects.get(id=admin )
        user = AdminProfile.objects.create(admin=admin_object)
        return redirect("home")

    return render(request, "hospital/admin_profile.html")


@csrf_exempt
def register_department(request):
    if request.method == "POST":

        department_name = request.POST.get("department_name")
        price = request.POST.get("price")
        department = Department.objects.create(department_name = department_name,
                                               price = price)
        
    all_departements = Department.objects.all()
    context = {"all_departements" : all_departements}
    print(all_departements)
        
    return render(request, "hospital/register_department.html", context)

@csrf_exempt
def doctor_department(request):
    if request.method == "POST":

        doctor = request.POST.get("doctor")
        doctor_and_department = request.POST.get("doctor_and_department")
        price = request.POST.get("price") 
        doctor_object = DoctorProfile.objects.get(id = doctor)
        doctor_and_department_object = Department.objects.get(id = doctor_and_department )
    
        DoctorAndDepartment.objects.create(doctor=doctor_object,
                                        doctor_and_department=doctor_and_department_object,
                                        price=price )
        
    queryset = DoctorAndDepartment.objects.all()
    context = {"queryset":queryset}

    return render(request, "hospital/doctor_department.html", context)
    

@csrf_exempt
def booking(request):
    if request.method == "POST":

        doctor_department = request.POST.get("doctor_department")
        patient = request.POST.get("patient")
        price = request.POST.get("price")
        booking_date = request.POST.get("booking_date")
        appointment_date = request.POST.get("appointment_date")
        appointment_type = request.POST.get("appointment_type")

        doctor_department_object = DoctorAndDepartment.objects.get(doctor_and_department_id = doctor_department)
        patient_object = PatientProfile.objects.get(patient_id = patient)
        print("////",patient_object)

        Booking.objects.create(doctor_department=doctor_department_object,
                                patient = patient_object, 
                                price=price,
                                booking_date = booking_date,
                                appointment_date=appointment_date,
                                appointment_type=appointment_type)
    all_booking = Booking.objects.all()
    context = {"all_booking" : all_booking}

    return render(request, "hospital/booking.html", context)


        








