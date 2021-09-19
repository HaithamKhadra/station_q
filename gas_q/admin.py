from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Appointment, CarMake

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  list_display = ('username', 'first_name', 'last_name', 'email')

class AppointmentAdmin(admin.ModelAdmin):
  list_display = ('user', 'car_make', 'car_num', 'timeslot')

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(User, UserAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(CarMake, CarMakeAdmin)
