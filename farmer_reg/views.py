from django.contrib.auth.models import User
from rest_framework import viewsets

from farmer_reg.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer