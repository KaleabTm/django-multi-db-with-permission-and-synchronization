# Generated by Django 5.1.3 on 2024-11-22 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobtitle',
            name='department',
        ),
    ]