from django.contrib.auth.models import AbstractUser
from django.db import models
from departments.models import Department, JobTitle

from common.models import BaseModel

# Create your models here.
class Employees(AbstractUser,BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=254)
    password = models.CharField(max_length=255)
    position = models.ForeignKey(JobTitle,on_delete=models.PROTECT, null=True)  # Roles like 'admin', 'editor', etc.
    department = models.ForeignKey(Department,on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = None  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    class Meta:
        verbose_name = ('Employee')
        verbose_name_plural = ('Employees')
        ordering = ('first_name', )

    def __str__(self):
        return self.email

    