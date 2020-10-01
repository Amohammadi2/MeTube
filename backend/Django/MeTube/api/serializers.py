from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Profile
        exclude = []