from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Appointment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  list_display = ('username', 'first_name', 'last_name', 'email')

class AppointmentAdmin(admin.ModelAdmin):
  list_display = ('user', 'car_make', 'car_num', 'day', 'timeslot')


admin.site.register(User, UserAdmin)
admin.site.register(Appointment, AppointmentAdmin)
