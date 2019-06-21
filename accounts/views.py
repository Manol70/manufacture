from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect



from .forms import SignUpForm
from . import models
# Create your views here.


def redirect_user(request):
    url = f'/orders/'
    return HttpResponseRedirect(url)


'''class SignUp(generic.CreateView):
    model = models.ProfileUser
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'''

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})