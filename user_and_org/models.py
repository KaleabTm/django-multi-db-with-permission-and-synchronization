# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Organizations(models.Model):
    org_name = models.CharField(max_length=255)
    org_email = models.CharField(max_length=255)
    org_phone_no = models.CharField(max_length=255)
    org_description = models.CharField(max_length=255, blank=True, null=True)
    org_domain = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizations'


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=254)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class UsersOrgs(models.Model):
    user = models.OneToOneField(Users, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, organization_id) found, that is not supported. The first column is selected.
    organization = models.ForeignKey(Organizations, models.DO_NOTHING)
    position = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_orgs'
        unique_together = (('user', 'organization'),)
