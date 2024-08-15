
from django.urls import path
from .views import *

urlpatterns = [
    path("complete-profile/", complete_profile, name="complete_profile"),
    path("get-profile/", get_profile, name="get_profile"),
    path("doctor-profile/", doctor_profile, name="doctor_profile"),
    path("get-doctor-profile/", get_doctor_profile, name="get-doctor-profile"),
    path("admin-profile/", admin_profile, name="admin_profile"),
    path("register-department/", register_department, name="register_department"),
    path("get-doctor-profile/", get_doctor_profile, name="get-doctor-profile"),
    path("doctor-department/", doctor_department, name="doctor_department"),
    path("booking/", booking, name="booking"),
]