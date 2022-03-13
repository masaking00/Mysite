from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from user.models import User
from api.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']