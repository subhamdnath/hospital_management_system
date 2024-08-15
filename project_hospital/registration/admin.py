from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser

class UserAdmin(BaseUserAdmin):

    list_display = ["id", "email", "name", "phone_number", "password", "gender", "date_of_birth",
                    "blood_group", "location", "marital_status", "role", "is_admin"]
    
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),

        ("Personal info", {"fields": ["name", "phone_number", "gender", "date_of_birth",
                    "blood_group", "location", "marital_status", "role"]}),

        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "phone_number", "gender", "date_of_birth",
                    "blood_group", "location", "marital_status", "role", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []



admin.site.register(MyUser, UserAdmin)

