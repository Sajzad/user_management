from django.db import models
from django.contrib import admin


class RequestLog(models.Model):
    username = models.CharField(max_length=150, null=True, default=None)
    method = models.CharField(max_length=8)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def create_log(cls, username: str, method: str):
        return cls.objects.create(
            username=username,
            method=method
        )
    

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ["username", "method", "timestamp"]