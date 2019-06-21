from django import forms
from django.core.validators import FileExtensionValidator, ValidationError
from datetime import datetime, date, timedelta

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import ModelForm
import magic


from . models import Orders, Customer, Glass, Type, TypeMontage, Statuses
from accounts.models import User




class CreateOrderForm(forms.ModelForm):
    quadrature = forms.DecimalField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    # by_date = forms.DateTimeField(initial=datetime.now, required=False, widget=forms.DateTimeInput(
    #     attrs={'class': 'form-control'}
    # ))
    for_date = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}))

    price = forms.DecimalField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}
    ))
    note = forms.Textarea(attrs={'class': 'form_control'})
    customer_id = forms.ModelChoiceField(queryset=Customer.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}
    ))
    glass_id = forms.ModelChoiceField(queryset=Glass.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}
    ))
    type_id = forms.ModelChoiceField(queryset=Type.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}
    ))
    type_montage_id = forms.ModelChoiceField(queryset=TypeMontage.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}
    ))
    user_id = forms.ModelChoiceField(queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}
    ))

    class Meta:
        model = Orders
        fields = ('quadrature', 'customer_id', 'price', 'note', 'glass_id', 'type_id', 'type_montage_id', 'user_id',
                  'for_date')

    def clean(self):
        cleaned_data = super(CreateOrderForm, self).clean()
        for_date = cleaned_data.get('for_date')

        if for_date < date.today():
            raise forms.ValidationError(
                "НЕВАЛИДНА ДАТА"
            )


class FilterForm(forms.Form):
    day_interval = timedelta(days=30)
    CHOICES = [('when_ordered', 'кога е поръчана'), ('when_ready', 'кога трябва да е готова')]
    CHOICES2 = [('all', 'Всички'), ('unpaid', 'само неплатени')]
    type_montage_id = forms.ModelChoiceField(TypeMontage.objects.all(), label='Тип монтаж',
                                          empty_label='Всички', required=False,
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    customer_id = forms.ModelChoiceField(Customer.objects.order_by('name'), required=False,
                                      label='Клиент', empty_label='Всички',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    type_id = forms.ModelChoiceField(Type.objects.all(),
                                  label='Тип', empty_label='Всички', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    glass_id = forms.ModelChoiceField(Glass.objects.all(),
                                   label='Стъклопакет', empty_label='Всички',required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    status_id = forms.ModelChoiceField(Statuses.objects.all(),required=False,
                                    label='Статус', empty_label='Всички',
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    paid = forms.ChoiceField(choices=CHOICES2, required=False,
                             label='Плащане:',
                             widget=forms.Select(attrs={'class': 'form-control'}))
    sort_by_date_orders = forms.ChoiceField(choices=CHOICES,
                                            label='Сортирай по:',
                                            widget=forms.RadioSelect)
    from_date = forms.DateField(required=True, label='От дата:',initial=date.today()-day_interval,
                                widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}))
    to_date = forms.DateField(required=True, label='До дата:', initial=date.today(),
                              widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}))

    def clean(self):
        cleaned_data = super(FilterForm, self).clean()
        from_date = cleaned_data.get('from_date')
        to_date = cleaned_data.get('to_date')

        if from_date is not None and to_date is not None:
            if from_date > to_date:
                raise forms.ValidationError(
                    "НЕКОРЕКТНА ДАТА"
                )


class UpdateScheme(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('scheme',)

    def clean(self):
        cleaned_data = super(UpdateScheme, self).clean()
        file = cleaned_data.get("scheme", False)
        filetype = magic.from_buffer(file.read(), mime=True)
        print(filetype)
        if "jpeg" not in filetype:
            raise ValidationError("File is not JPEG")




