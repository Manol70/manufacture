from django.shortcuts import render

from django.views import generic
from . import models
from . import forms
# Create your views here.


class CustomerList(generic.ListView):
    model = models.Customer
    template_name = 'customer_list.html'
    context_object_name = 'customer'

    def get_queryset(self):
        customers = models.Customer.objects.all()
        return customers


class NewCustomer(generic.CreateView):
    model = models.Customer
    template_name = 'new_customer.html'
    form_class = forms.CreateCustomerForm
    success_url = '/customers/'


class CustomerEdit(generic.UpdateView):
    model = models.Customer
    form_class = forms.CreateCustomerForm
    template_name = 'new_customer.html'
    success_url = '/customers/'
