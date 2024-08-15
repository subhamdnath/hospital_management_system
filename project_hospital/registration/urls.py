
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", login_user, name="login_user"),
    path('signup/', signup, name = "signup"),
    path('change-password/', change_password, name = "change_password"),
    path("home/", home, name="home"),
    path("logout/", logout_user, name = "logout_user"),
]
