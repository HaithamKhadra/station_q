# Generated by Django 3.2.7 on 2021-09-19 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_q', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='nomatch', message='8 nums', regex='^[0-9]{8}')]),
        ),
    ]