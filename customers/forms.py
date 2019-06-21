from django import forms
from django.core.validators import RegexValidator, validate_email

from .models import Customer


class CreateCustomerForm(forms.ModelForm):
    name = forms.CharField(required=True,label='Име', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    town = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    phone1 = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    required=False, widget=forms.TextInput(
                                        attrs={
                                            'class': 'form-control'
                                        }
    ))
    phone2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    mail = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    note = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Customer
        fields = ('id', 'name', 'town', 'address', 'phone1', 'phone2', 'mail', 'note')
