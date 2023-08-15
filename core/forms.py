from django import forms
from .models import customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        # fields = '__all__'
        fields = (
            'name',
            'dob',
            'mobile',
            'email',
            'father_name',
            'mother_name',
            'married_status',
            'nominee',
            'aadhar',
            'pan',
            'address',
            'pin',
            'pan_image',
            'passport_image',
            'aadhar_front_image',
            'aadhar_back_image',
            'signeture_image',
            'account_status',
        )