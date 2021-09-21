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
        (00, '08:30 – 09:00'),
        (10, '09:00 – 09:30'),
        (11, '09:30 – 10:00'),
        (12, '10:00 – 10:30'),
        (13, '10:30 – 11:00'),
        (14, '11:00 – 11:30'),
        (15, '11:30 – 12:00'),
        (16, '12:00 – 12:30'),
        (17, '12:30 – 01:00'),
        (18, '01:00 – 01:30'),
        (19, '01:30 – 02:00'),
        (20, '02:00 – 02:30'),
        (21, '02:30 – 03:00'),
        (22, '03:00 – 03:30'),
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
                max_length=8,
                blank=True,
                validators=[RegexValidator(
                    regex='^[0-9]{8}', 
                    message='8 nums', 
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