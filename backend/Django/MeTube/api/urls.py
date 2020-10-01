from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path("users/get-auth-token/", obtain_auth_token, name="get-auth-token"),
    path("users/get-profile/", RetrieveUpdateUserProfile.as_view(), name="get-profile")
]