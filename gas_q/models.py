from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

# class CarMake(models.Model):
#     name = models.CharField(max_length=64)
#     slug = models.SlugField()

#     def __str__(self):
#         return self.name
     

class Appointment(models.Model):

    class Meta:
        unique_together = ('user', 'timeslot')

    TIMESLOT_LIST = (
        (None, 'الأوقات'),
        (0, '08:30 – 09:00'),
        (1, '09:00 – 09:30'),
        (2, '09:30 – 10:00'),
        (3, '10:00 – 10:30'),
        (4, '10:30 – 11:00'),
        (5, '11:00 – 11:30'),
        (6, '11:30 – 12:00'),
        (7, '12:00 – 12:30'),
        (8, '12:30 – 01:00'),
    )

    DAYS = (
        (None, 'الأيام'),
        (0, 'الأثنين'),
        (1, 'الثلاثاء'),
        (2, 'الأربعاء'),
    )


    user = models.OneToOneField(
                User, 
                on_delete=models.CASCADE, 
                default=None, 
                null=True, 
                related_name='user'
    )
    car_make = models.CharField(max_length=24, blank=False)
    phone_number = models.CharField(
                max_length=8,
                blank=True,
                validators=[RegexValidator(
                    regex='^[0-9]{8}', 
                    message='8 nums', 
                    code='nomatch')]
    )
    car_num = models.CharField(
                max_length=7,
                validators=[RegexValidator(
                    regex='^[A-Za-z][0-9]{1,6}$', 
                    message='Length has to be 1 letter, and 1 to 6 nums', 
                    code='nomatch')]
    )
    day = models.IntegerField(choices=DAYS,default=None)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST, default=None)


    def __str__(self):
        return self.user.username 

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "car_make": self.car_make,
            "car_num": self.car_num,
            "phone_number": self.phone_number,
            "timeslot": self.timeslot, 
            "day": self.day
        }