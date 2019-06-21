from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('profile/', views.redirect_user, name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]