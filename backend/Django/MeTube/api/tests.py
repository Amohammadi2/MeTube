from io import BytesIO
from json import dumps
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *


class AuthenticationSystemTest (TestCase):

    def setUp(self):
        """create the database records needed"""
        User.objects.create_user(username="tester-1", password="some-secret")
        User.objects.create_user(username="tester-2", password="some-secret")
        User.objects.create_user(username="tester-3", password="some-secret")

    def test_users_have_token(self):
        """ test all the users have authentication token
        test the signals receiver are working properly
        """
        for user in User.objects.all():
            token = user.auth_token
            self.assertIsInstance(token, Token)

    def test_users_are_authenticated(self):
        """ test all the users can login using their user name and password """
        actual_user = get_object_or_404(User, id=1)
        response = self.client.post(reverse("get-auth-token"), {
            "username": "tester-1",
            "password": "some-secret",
        })
        self.assertEqual(response.data["token"], actual_user.auth_token.key)
        response = self.client.post(reverse("get-auth-token"), {
            "username": "tester-1",
            "password": "wrong-password",
        })
        self.assertNotIn("token", response.data.keys())
        self.assertIn("non_field_errors", response.data.keys())


class UserProfileTest (TestCase):

    def setUp(self):
        User.objects.create_user(username="test-1", password="some-secret")
        User.objects.create_user(username="test-2", password="some-secret")
        User.objects.create_user(username="test-3", password="some-secret")

    def test_all_users_have_profile(self):
        for user in User.objects.all():
            self.assertIsInstance(user.profile, Profile)

    def test_users_can_get_their_profiles(self):
        user = User.objects.all()[0]
        print (user.auth_token.key)
        print (f"Token {user.auth_token.key}")
        headers = {
            "HTTP_AUTHORIZATION": f"Token {user.auth_token.key}"
        }
        profile = self.client.get(reverse("get-profile"), **headers)
        self.assertJSONEqual(
            dumps(profile.data),
            ProfileSerializer(user.profile).data
        )