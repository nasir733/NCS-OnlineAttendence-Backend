# Generated by Django 3.2.7 on 2021-09-10 08:23

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_useraccount_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='last_matched_image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.last_matched_wrapper),
        ),
    ]
