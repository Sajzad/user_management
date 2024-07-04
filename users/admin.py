from django.contrib import admin
from users.models import User
# from django.contrib.auth.admin import UserAdmin


# class CustomUserAdmin(admin.ModelAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     # model = User
#     list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active',)
#     list_filter = ('user_type', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('username', 'password', 'email', 'first_name', 'last_name', 'user_type')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('username', 'email',)
#     ordering = ('username',)


# admin.site.register(User, CustomUserAdmin)