from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Access(models.Model):
    access_level = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.access_level}'


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_level = models.ForeignKey(Access, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} has access level {self.access_level}'

