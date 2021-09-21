# Generated by Django 3.2.7 on 2021-09-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_q', '0002_alter_appointment_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='day',
            field=models.IntegerField(choices=[(None, 'الأيام'), (0, 'اثنين'), (1, 'الثلاثاء'), (2, 'الالرتسي')], default=None),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='timeslot',
            field=models.IntegerField(choices=[(None, 'اخشسبيشسبشيبش'), (0, '08:30 – 09:00'), (1, '09:00 – 09:30'), (2, '09:30 – 10:00'), (3, '10:00 – 10:30'), (4, '10:30 – 11:00'), (5, '11:00 – 11:30'), (6, '11:30 – 12:00'), (7, '12:00 – 12:30'), (8, '12:30 – 01:00')], default=None),
        ),
    ]