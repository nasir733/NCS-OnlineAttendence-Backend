# Generated by Django 3.2.7 on 2021-09-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_useraccount_profile_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]
