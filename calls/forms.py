from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ClientRequest

class CallRegisterForm(forms.ModelForm):

    class Meta:
        model = ClientRequest
        fields = [
            'client', 
            'server',
            'required_date',
            'description_of_category',
            'detail',
            'requester',
        ]

class CallUpdateForm(forms.ModelForm):

    class Meta:
        model = ClientRequest
        fields = [
            'client', 
            'server',
            'required_date',
            'description_of_category',
            'detail',
            'requester',
        ]


