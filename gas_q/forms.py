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
        fields = ['user', 'phone_number', 'place', 'car_make', 'car_num', 'day', 'timeslot']

        widgets = {
            'user': TextInput(attrs={
                'class': 'form-control py-1 mb-3',
                'placeholder': 'الأسم'
            }),
            'place': TextInput(attrs={
                'class': 'form-control py-1 mb-3',
                'placeholder': 'مكان السكن'
            }),
            'car_make': TextInput(attrs={
                'class': 'form-control py-1 mb-3',
                'placeholder': 'اسم السياره'
            }),
            'day': Select(attrs={
                # 'style': 'max-width: 400px;',
                'class':'day_options form-select',
            }),
            'timeslot': Select(attrs={
                'label': 'بتبتبتبت',
                'class':'hour_options form-select',
            }),
            'car_num': TextInput(attrs={
                'class': 'form-control py-1 mb-2',
                'placeholder': 'car number'
            }), 
            'phone_number': TextInput(attrs={
                'class': 'form-control py-1 mb-3',
                'placeholder': 'مثال: 12345678'
            }), 
        }



