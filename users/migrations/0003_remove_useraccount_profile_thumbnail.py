# Generated by Django 3.2.7 on 2021-09-10 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_useraccount_profile_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='profile_thumbnail',
        ),
    ]