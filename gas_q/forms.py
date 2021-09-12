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
        fields = ['car_make', 'car_num', 'timeslot']
        widgets = {
            'car_make': Select(attrs={
                'style': 'max-width: 400px;',
            }),
            # 'timeslot': Select(attrs={
            #     'style': 'max-width: 400px;',
            # }),
            'car_num': TextInput(attrs={
                'style': 'max-width: 400px;',
                'placeholder': 'car number'
            }), 
        }



