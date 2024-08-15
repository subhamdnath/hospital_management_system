from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, phone_number, password, gender, date_of_birth,
                    blood_group, location, marital_status, role):
        if not email:
            raise ValueError("User must have an email")
        
        user = self.model(email = self.normalize_email(email),
                          name = name, phone_number = phone_number,
                          password = password, gender = gender, date_of_birth = date_of_birth,
                          blood_group = blood_group, location = location,
                            marital_status = marital_status, role = role )
        
        user.save(using = self._db)
        return user

    def create_superuser(self, name, email, phone_number, password, gender, date_of_birth,
                    blood_group, location, marital_status):
        user = self.create_user(name = name, email = email, phone_number = phone_number,
                          password = password, gender = gender, date_of_birth = date_of_birth,
                          blood_group = blood_group, location = location,
                            marital_status = marital_status, role = "admin" )
        user.is_admin = True
        user.set_password(password)
        user.save(using = self._db)
        return user
    
class MyUser(AbstractBaseUser):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, verbose_name="email address")
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(("Male","Male"),
                                                      ("Female","Female"),
                                                      ("Other","Other")))
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=5, blank=True)
    location = models.CharField(max_length=40)
    marital_status = models.CharField(max_length=20, choices=(("Married","Married"),
                                                              ("Single","Single"),
                                                              ("Others","Other")))
    
    role = models.CharField(max_length=20, choices=(("Doctor","Doctor"),
                                                    ("Nurse","Nurse"),
                                                    ("Admin", "Admin"),
                                                    ("Patient","Patient")))

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =  ["name", "phone_number","gender", "date_of_birth",
                    "blood_group", "location", "marital_status",]
   
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin