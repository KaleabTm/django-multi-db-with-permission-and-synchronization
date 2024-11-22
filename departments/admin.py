from django.contrib import admin
from .models import Department, JobTitle


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = [
        'department_name',
        'description',
        'contact_phone',
        'contact_email',
        ]
    search_fields = ('department_name','contact_email')
    ordering = ('-department_name',)
    
    fieldsets = (
        (None, {'fields': ('department_name',)}),
        ('Department Info', {'fields':('description',)}),
        ('Contacts',{'fields': ('contact_phone', 'contact_email')}),
        ('Activity',{'fields': ('is_active',)}),

    )


class JobTitlentAdmin(admin.ModelAdmin):
    model = JobTitle
    list_display = [
        'title',
        ]

admin.site.register(Department, DepartmentAdmin)

admin.site.register(JobTitle)

