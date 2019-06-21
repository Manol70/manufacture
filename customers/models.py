from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=20)
    town = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=20, blank=True)
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    mail = models.EmailField(blank=True)
    note = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.name}'

