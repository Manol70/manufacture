# Generated by Django 2.2 on 2019-06-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orders_scheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]