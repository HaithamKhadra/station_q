from re import template
from django.contrib.auth import models
from django.db.models import fields
from django.forms import TextInput, Select
from django.forms import widgets
from django.forms.widgets import TextInput
from .models import Appointment
from django import forms


class CreateForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['phone_number', 'car_make', 'car_num', 'timeslot', 'day']
        widgets = {
            'car_make': TextInput(attrs={
                'style': 'max-width: 400px;',
                'placeholder': 'اسم السياره'
            }),
            'day': Select(attrs={
                'style': 'max-width: 400px;',
                'class':'day_options',
            }),
            'timeslot': Select(attrs={
                'style': 'max-width: 400px;',
                'class':'hour_options',
            }),
            'car_num': TextInput(attrs={
                'style': 'max-width: 400px;',
                'placeholder': 'car number'
            }), 
            'phone_number': TextInput(attrs={
                'style': 'max-width: 400px;',
                'placeholder': 'مثال: 12345678'
            }), 
        }



