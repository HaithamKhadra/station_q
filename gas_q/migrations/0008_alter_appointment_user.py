# Generated by Django 3.2.7 on 2021-09-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_q', '0007_alter_appointment_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
