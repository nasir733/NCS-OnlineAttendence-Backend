# Generated by Django 3.2.7 on 2021-09-26 13:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0007_alter_faceencoding_encodings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faceencoding',
            name='encodings',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None), blank=True, null=True, size=None),
        ),
    ]
