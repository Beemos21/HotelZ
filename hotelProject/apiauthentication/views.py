from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
import os

from rest_framework.permissions import IsAuthenticated


# Class based view to register user

class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(UpdateAPIView):
    """
        An endpoint for changing password.
        """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            # return Response(status=status.HTTP_205_RESET_CONTENT)
            response1 = {
                'status': 'success',
                'message': 'token black listed successfully',
            }
            return Response(response1)
        except Exception as e:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            response2 = {
                # 'status': 'success',
                'message': 'you are logged out (your refresh_token is black listed)',
            }
            return Response(response2)
