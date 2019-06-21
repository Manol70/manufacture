from django import forms
from . import models
from .models import Customer

from django.http import HttpResponseRedirect
from django.shortcuts import render


def test(request):
    customer_id = request.POST.customer
    return customer_id

class CreatePaymentForm(forms.ModelForm):
    paid = forms.DecimalField(required=True, widget=forms.TextInput)
    document = forms.CharField(widget=forms.TextInput)
    number_doc = forms.IntegerField(widget=forms.TextInput)

    # def clean(self):
    #     if self.paid>self.request.POST['balance']:
    #         raise forms.ValidationError('KELD.ROKF')


    class Meta:
        model = models.Payment
        fields = ('paid', 'document', 'number_doc')
