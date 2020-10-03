from django.shortcuts import render
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from .permissions import IsOwner
# Create your views here.

class RetrieveUpdateUserProfile (GenericAPIView, RetrieveModelMixin):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]

    def get_object(self):
        return self.request.user.profile

    def get(self, request, *args, **kwargs):
        print (request.user)
        if not isinstance(request.user, AnonymousUser):
            return self.retrieve(request, *args, **kwargs)
        return Response({"error": "user credentialsare not provided"}, HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk, *args, **kwargs):
        if not isinstance(request.user, AnonymousUser):
            profile_to_update = self.get_object()
            self.check_object_permissions(request, profile_to_update)
            return Response(self.get_serializer_class()(profile_to_update).data)
        return Response({"error": "user credentialsare not provided"}, HTTP_401_UNAUTHORIZED)