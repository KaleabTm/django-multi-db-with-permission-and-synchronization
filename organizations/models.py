from django.db import models

from common.models import BaseModel


class OurOrganizations(BaseModel):
    org_name = models.CharField(max_length=255)
    org_email = models.CharField(max_length=255)
    org_phone_no = models.CharField(max_length=255)
    org_description = models.CharField(max_length=255, blank=True, null=True)
    org_domain = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ('Organization')
        ordering = ('org_name',)
        db_table = 'organizations_ourorganizations'

    def __str__(self):
        return self.org_name
