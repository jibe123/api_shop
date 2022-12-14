from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
