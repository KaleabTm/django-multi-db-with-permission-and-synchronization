from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employees

class CustomUserAdmin(UserAdmin):
    model = Employees
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Job Info', {'fields': ('department','position')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name','phone_number', 'is_staff', 'is_active'),
        }),
    )

    # Ensure 'username' is excluded
    exclude = ('username',)


admin.site.register(Employees, CustomUserAdmin)
