from django.urls import path
from django.urls import path 
from users.views import (
    RegisterUser,
    LoginUser,
    logout_user,
)

urlpatterns = [
    path("register/", RegisterUser, name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
]
