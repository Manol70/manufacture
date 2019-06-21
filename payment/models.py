from django.db import models

from datetime import datetime

from accounts.models import User
from orders.models import Orders, TypeMontage
from customers.models import Customer

# Create your models here.
class Payment(models.Model):
    orders_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type_montage = models.ForeignKey(TypeMontage, on_delete=models.CASCADE)
    paid = models.DecimalField(max_digits=6, decimal_places=2,)
    data_paid = models.DateTimeField(default=datetime.now, blank=True)
    document = models.CharField(max_length=255, blank=True)
    number_doc = models.IntegerField(blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)