from django.shortcuts import render, redirect

from .forms import UserCreateForm


def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('login-page')
    else:
        signup_form = UserCreateForm()
    return render(request, 'signup/signup-page.html', {'form': signup_form})

def loginpage(request):
    return render(request, 'signup/login-page.html')

#testadmin