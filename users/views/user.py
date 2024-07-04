from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from users.permissions import IsManager, IsCustomer
from users.authentication import TokenAuthentication
from rest_framework.decorators import action
from users.models import User
from users.serializers import UserSerializer, FetchUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsCustomer()]
        return [IsManager()]
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return FetchUserSerializer
        return UserSerializer