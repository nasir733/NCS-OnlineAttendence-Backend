# Generated by Django 3.2.7 on 2021-09-10 07:00

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_useraccount_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=users.models.wrapper),
        ),
    ]