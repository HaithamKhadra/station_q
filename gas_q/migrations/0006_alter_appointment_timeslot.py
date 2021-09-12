# Generated by Django 3.2.7 on 2021-09-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_q', '0005_alter_appointment_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeslot',
            field=models.IntegerField(choices=[(None, 'Your String For Display'), (0, '09:00 – 09:30'), (1, '10:00 – 10:30'), (2, '11:00 – 11:30'), (3, '12:00 – 12:30'), (4, '13:00 – 13:30'), (5, '14:00 – 14:30')], default=0),
        ),
    ]
