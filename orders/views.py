from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic, View
from django.db.models import F, ExpressionWrapper
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import date
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render, redirect
from . models import Type, Orders, TypeMontage, Glass, Statuses
from customers.models import Customer
from . forms import CreateOrderForm, FilterForm, UpdateScheme





class CreateOrderForm(generic.CreateView):
    model = Orders
    template_name = 'create_order.html'
    form_class = CreateOrderForm
    success_url = '/orders/'


def orders_list(request):
    type_montage = request.POST['type_montage_id']
    customer = request.POST['customer_id']
    type = request.POST['type_id']
    glass = request.POST['glass_id']
    status = request.POST['status_id']
    balance = request.POST['paid']
    sort_by_date = request.POST['sort_by_date_orders']



    if type_montage is not '':
        typeMontageFilter = Orders.objects.filter(type_montage_id=type_montage)
    else:
        typeMontageFilter = Orders.objects.filter()
    if customer is not '':
        customerFilter = Orders.objects.filter(customer_id=customer)
    else:
        customerFilter = Orders.objects.filter()
    if type is not '':
        typeFilter = Orders.objects.filter(type_id=type)
    else:
        typeFilter = Orders.objects.filter()
    if glass is not '':
        glassFilter = Orders.objects.filter(glass_id=glass)
    else:
        glassFilter = Orders.objects.filter()
    if status is not '':
        statusFilter = Orders.objects.filter(status_id=status)
    else:
        statusFilter = Orders.objects.filter()
    if balance == 'unpaid':
       balance = Orders.objects.annotate(diff=(F('price') - F('paid'))).filter(diff=0)
    else:
        balance = Orders.objects.filter()
    if sort_by_date=='when_ordered':
        orderList = typeMontageFilter & customerFilter & typeFilter & glassFilter & statusFilter & balance.order_by('-by_date')
    else:
        orderList = typeMontageFilter & customerFilter & typeFilter & glassFilter & statusFilter & balance.order_by('-for_date')

    return orderList

def orders_list2(request):
    postList = request.POST
    for key, value in postList.iteritems():
        if key is not 'csrfmiddlewaretoken':
            if value is not '':
                keyFilter = Orders.objects.filter()



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)


        # create a form instance and populate it with data from the request:
        form = FilterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
                # request.POST['to_date'] = date.today()
            print(request.POST)
            # ordersList= Orders.objects.filter(type_montage_id>0)
            ordersList = orders_list(request)
            # redirect to a new URL:
            # print(request.path_info)
            return render(request, 'orders.html', {'form': form, 'sentForm': True, 'orders': ordersList, 'paid':222, 'typ':type})
            # return HttpResponseRedirect(request.path_info)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilterForm()

    return render(request, 'orders.html', {'form': form})


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')


def scheme_upload(request):
    id = request.GET.get('id')
    if request.method == 'POST':
        order = Orders.objects.get(pk=id)
        form = UpdateScheme(request.POST, request.FILES, instance=order)
        print(request.FILES)

        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = UpdateScheme()
    return render(request, 'upload.html', {
        'form': form
    })
