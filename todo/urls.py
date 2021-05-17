from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path('create/',views.create , name='create'),

    path('registerpage/',views.registerpage, name='registerpage'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logout/',views.logoutuser, name='logout'),
]