from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Department(BaseModel):
    department_name = models.CharField(max_length=255, verbose_name=_("Department Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    contact_phone = models.PositiveBigIntegerField(blank=True, null=True, verbose_name=_("Contact Phone"))
    contact_email = models.EmailField(blank=True, null=True, verbose_name=_("Contact Email"))
    is_acitve = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.department_name}"

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")
        permissions = [
           ( 'can_create_department', 'Can Create Department'),
           ('can delete_department', 'Can Delete Department'),
           ('can edit_department','Can Edit Department'),
           ('can_close_department','Can Close Department'),
        ]


class JobTitle(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255, verbose_name=_("Job Title"))

    def __str__(self):
        return f"{self.title}"