from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Restaurant, UserRole, City, Company, OilCollector, OilCollectContract
from .choices import (
    dict1,
    TUPLE2_CLIENT_REQUESTS ,
    TUPLE2_UINT_SYMBOLS,
    TUPLE1_PAID_METHODS,
    TUPLE1_PROCESSING_STATUS,
    TUPLE2_USER_ROLES,
)

class RestaurantRegisterForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = [
            'short_name', 
            'full_name',
            'image',
            'phone',
            'division',
            'latitude',
            'longitude',
            'is_active',
            'unit_number',
            'street',
            'city',
            'postal_code', 
            # 'staffs',
            # 'registered_on',
            'approved_on',
        ]

class RestaurantUpdateForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = [
            'short_name', 
            'full_name',
            'image',
            'phone',
            'division',
            'latitude',
            'longitude',
            'is_active',
            'unit_number',
            'street',
            'city',
            'postal_code', 
            # 'staffs',
            # 'registered_on',
            'approved_on',
        ]


class UserRoleCreateForm ( forms.ModelForm):
    # user = forms.CharField()
    # company = forms.CharField()
    # role = forms.MultipleChoiceField(
    #     choices=TUPLE2_USER_ROLES,
    #     # default=1,
    # )
    class Meta:
        model = UserRole
        fields = [
            'user', 
            'company',
            'role',
        ]



    # test= forms.MultipleChoiceField(choices=TEST_CHOICES, required=False)
    