from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
     

class Appointment(models.Model):

    class Meta:
        unique_together = ('user', 'timeslot')

    TIMESLOT_LIST = (
        (None, 'الأوقات'),
        (10, '08:30 – 09:00'),
        (11, '09:00 – 09:30'),
        (12, '09:30 – 10:00'),
        (13, '10:00 – 10:30'),
        (14, '10:30 – 11:00'),
        (15, '11:00 – 11:30'),
        (16, '11:30 – 12:00'),
        (17, '12:00 – 12:30'),
        (18, '12:30 – 01:00'),
        (19, '01:00 – 01:30'),
        (20, '01:30 – 02:00'),
        (21, '02:00 – 02:30'),
        (22, '02:30 – 03:00'),
        (23, '03:00 – 03:30'),
    )

    DAYS = (
        (None, 'الأيام'),
        (0, 'الأثنين'),
        (1, 'الثلاثاء'),
        (2, 'الأربعاء'),
    )


    user = models.CharField(max_length=64, blank=False)
    # user = models.OneToOneField(
    #             User, 
    #             on_delete=models.CASCADE, 
    #             default=None, 
    #             null=True, 
    #             related_name='user'
    # )
    car_make = models.CharField(max_length=24, blank=False)
    phone_number = models.CharField(
                max_length=9,
                blank=True,
                validators=[RegexValidator(
                    regex='^[0-9]{2}-[0-9]{6}', 
                    message='must be 8 numbers for example: 03-xxxxxx', 
                    code='nomatch')]
    )
    place = models.CharField(max_length=24, blank=False, null=True)
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
        return self.user

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "car_make": self.car_make,
            "car_num": self.car_num,
            "phone_number": self.phone_number,
            'place': self.place,
            "day": self.day,
            "timeslot": self.timeslot, 
        }