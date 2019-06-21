from django.contrib import admin

from . import models
# Register your models here.


admin.site.register(models.Glass)
admin.site.register(models.Type)
admin.site.register(models.TypeMontage)
admin.site.register(models.Statuses)
admin.site.register(models.Orders)