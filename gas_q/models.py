from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class CarMake(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()

    def __str__(self):
        return self.name
     

class Appointment(models.Model):

    class Meta:
        unique_together = ('user', 'timeslot')

    TIMESLOT_LIST = (
        (None, 'اخشسبيشسبشيبش'),
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
    )

    user = models.OneToOneField(
                User, 
                on_delete=models.CASCADE, 
                default=None, 
                null=True, 
                related_name='user'
    )

    car_make = models.ForeignKey(
                CarMake, 
                on_delete=models.CASCADE,
                default=0, 
                null=True,
                related_name='car_make'
    )

    car_num = models.CharField(
                max_length=7,
                validators=[RegexValidator(
                    regex='^[A-Za-z][0-9]{1,6}$', 
                    message='Length has to be 1 letter, and 1 to 6 nums', 
                    code='nomatch')]
    )
    timeslot = models.IntegerField(choices=TIMESLOT_LIST, default=0)


    def __str__(self):
        return self.user.username 

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "car_make": self.car_make.name,
            "car_num": self.car_num,
            "timeslot": self.timeslot
        }


# class TimeSlot(models.Model):

#     class Meta:
#         unique_together = ('user', 'date', 'timeslot')

#     TIMESLOT_LIST = (
#         (0, '09:00 – 09:30'),
#         (1, '10:00 – 10:30'),
#         (2, '11:00 – 11:30'),
#         (3, '12:00 – 12:30'),
#         (4, '13:00 – 13:30'),
#         (5, '14:00 – 14:30'),
#     )

#     user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user_time_slot')
#     timeslot = models.IntegerField(choices=TIMESLOT_LIST)

#     # date = models.DateField(help_text="YYYY-MM-DD")
#     # timeslot = models.ManyToManyField(Appointment, related_name='time')

#     def __str__(self):
#         return self.user.username + '-' + self.timeslot.timeslot

#     # @property
#     # def time(self):
#     #     return self.TIMESLOT_LIST[self.timeslot][1]

