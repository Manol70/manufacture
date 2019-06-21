from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.FilterOrders.as_view(), name='filter'),
    path('', views.get_name, name='orders'),
    path('upload/', views.scheme_upload, name='upload'),
    path('create_order/', views.CreateOrderForm.as_view(), name='create_order')
]

