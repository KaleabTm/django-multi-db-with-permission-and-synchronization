# Generated by Django 5.1.3 on 2024-11-22 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourorganizations',
            options={'ordering': ('org_name',), 'verbose_name': 'Organization'},
        ),
    ]
