from django.db import models
from datetime import datetime
from django.utils.timezone import now

from customers.models import Customer
from accounts.models import User

# Create your models here.


class Glass(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Statuses(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class TypeMontage(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type_montage_id = models.ForeignKey(TypeMontage, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    quadrature = models.DecimalField(max_digits=5, decimal_places=2)
    by_date = models.DateTimeField(default=datetime.now, blank=True)
    for_date = models.DateField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    glass_id = models.ForeignKey(Glass, on_delete=models.CASCADE, blank=True)
    status_id = models.ForeignKey(Statuses, on_delete=models.CASCADE, default=1)
    scheme = models.FileField(upload_to='media/', blank=True)
    note = models.CharField(max_length=255, blank=True)





