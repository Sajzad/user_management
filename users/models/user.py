import string
import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin


class UserTypes(models.TextChoices):
    MANAGER = 'manager', 'Manager'
    CUSTOMER = 'customer', 'Customer'

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

class User(AbstractUser):
    user_type = models.CharField(
        max_length=10,
        choices=UserTypes.choices,
        default=UserTypes.CUSTOMER
    )
    authentication_token = models.CharField(max_length=16, default=generate_token, unique=True)
    
    @classmethod
    def get(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None
    

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'authentication_token', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    ordering = ('-id',)