from django.urls import path, re_path

from . import views
urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer'),
    path('new_customer/', views.NewCustomer.as_view(), name='new-customer'),
    re_path('^edit/(?P<pk>\d+)/$', views.CustomerEdit.as_view(), name='customer-edit')
]