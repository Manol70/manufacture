# Generated by Django 2.2 on 2019-05-23 18:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMontage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('quadrature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('by_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('for_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('note', models.CharField(blank=True, max_length=255)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('glass_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Glass')),
                ('status_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Statuses')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Type')),
                ('type_montage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.TypeMontage')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
