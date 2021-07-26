from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.loginpage, name='login-page'),
    path('', views.home, name='home-page')
]