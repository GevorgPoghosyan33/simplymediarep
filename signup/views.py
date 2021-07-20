from django.shortcuts import render

def signup(request):
    return render(request, 'signup/signup-page.html')

def loginpage(request):
    return render(request, 'signup/login-page.html')

