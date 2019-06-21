from django.shortcuts import render
from django.views import generic
from django.db.models import F
from . import models
from . import forms
from .models import Customer, TypeMontage, Orders, User
# Create your views here.


class CreatePayment(generic.CreateView):
    model = models.Payment
    template_name = 'payment.html'
    form_class = forms.CreatePaymentForm
    success_url = 'payment.html'

    def form_valid(self, form):
        print(form)
        paid = self.request.POST['paid']
        balance = self.request.POST['balance']
        print(paid)
        print(balance)
        if paid>balance:
            return render(self.request, 'payment.html',{'form':form})
        customer = self.request.POST['customer_id']
        form.instance.customer_id = Customer.objects.get(name=customer)

        type_montage = self.request.POST['type_montage']
        form.instance.type_montage = TypeMontage.objects.get(name=type_montage)

        order_id = self.request.POST['orders_id']
        form.instance.orders_id = Orders.objects.get(pk=order_id)

        user = self.request.user.id
        form.instance.user_id = User.objects.get(pk=user)

        paidFieldOrders = Orders.objects.filter(id=order_id)
        paidFieldOrders.update(paid=F('paid') + paid)
        return super().form_valid(form)


