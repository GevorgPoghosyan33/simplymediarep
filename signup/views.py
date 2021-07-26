from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserForm


def home(request):
    return render(request, 'signup/home.html')

def signup(request):
    if request.method == 'POST':
        signup_form = NewUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home-page')
    else:
        signup_form = NewUserForm()
    return render(request, 'signup/signup-page.html', {'form': signup_form})

def loginpage(request):
    if request.method == 'POST':
        signup_form = AuthenticationForm(request, data=request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data.get('username')
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home-page')
    else:
        signup_form = AuthenticationForm()
    return render(request, 'signup/login-page.html', {'form': signup_form})

#testadmin