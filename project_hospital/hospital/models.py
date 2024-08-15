from django.db import models
from registration.models import *

class DoctorProfile(models.Model):

    doctor = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    experience = models.IntegerField()
    specialization = models.CharField(max_length=100)
    doctor_fee = models.DecimalField(max_digits=10, decimal_places=2)
    language = models.CharField(max_length=20)
    available_timings = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.experience} years"

class PatientProfile(models.Model):
    patient = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    emergency_contact = models.CharField(max_length=15, unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {self.patient.email}"
    
    def clean(self):
       
        if self.patient.role != 'Patient':
            raise ValueError('Only users with role "Patient" can have a PatientProfile.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    

class Department(models.Model):

    department_name = models.CharField(max_length=20, choices = (("Cardiology","Cardiology"),
                                                                 ("ENT","ENT"),
                                                                  ("General Physician","General Physician")))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.department_name
 

class DoctorAndDepartment(models.Model):

    class Meta:
        unique_together = (("doctor", "doctor_and_department"),)
    doctor = models.OneToOneField(DoctorProfile, on_delete=models.CASCADE, related_name="doctorandservice")
    doctor_and_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="doctorandservice")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctor.doctor.email} - {self.doctor_and_department.department_name}"
    
class Booking(models.Model):

    doctor_department = models.ForeignKey(DoctorAndDepartment, on_delete=models.CASCADE, related_name="bookings")
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateField()
    appointment_type = models.CharField(max_length=20, choices=(("Digital consult", "Digital consult"),
                                                                ("Hospital visit","Hospital visit")))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by{self.patient.patient.email} with {self.doctor_department.doctor.doctor.email}"

    @property
    def about_doctor(self):
        return self.doctor_department.doctor.about_doctor
    

class AdminProfile(models.Model):

    admin = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="admin")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.name} - {self.admin.email}"

















