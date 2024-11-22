# Generated by Django 5.1.3 on 2024-11-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_jobtitle_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='is_acitve',
        ),
        migrations.AddField(
            model_name='department',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
