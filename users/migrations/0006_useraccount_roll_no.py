# Generated by Django 3.2.7 on 2021-09-10 07:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_useraccount_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='roll_no',
            field=models.CharField(default=datetime.datetime(2021, 9, 10, 7, 3, 24, 945168, tzinfo=utc), max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
