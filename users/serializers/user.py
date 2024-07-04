from rest_framework import serializers
from users.models import User


class FetchUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'date_joined']
        

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'authentication_token']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'write_only': True},
            'email': {'write_only': True},
            'authentication_token': {'read_only': True},
        }