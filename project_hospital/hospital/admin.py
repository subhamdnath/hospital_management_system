from django.contrib import admin
from hospital.models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display =  [
    'department_name',
    'price',
    'created_on',
    'updated_on'
]

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = [
    "id",
    'doctor',
    'experience',
    'specialization',
    'doctor_fee',
    'language',
    'available_timings',
    'created_on',
    'updated_on'
]
    
@admin.register(DoctorAndDepartment)
class DoctorAndDepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "doctor", "doctor_and_department", "price", "created_on", "updated_on"]

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ["patient", "emergency_contact", "created_on", "updated_on"]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["doctor_department", "patient", "price", "booking_date", "appointment_date", "appointment_type", "created_on", "updated_on"]

@admin.register(AdminProfile)
class DAdminProfileAdmin(admin.ModelAdmin):
    list_display = ["admin", "created_on", "updated_on"]
