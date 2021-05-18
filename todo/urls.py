from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path('create/',views.create , name='create'),
    path('<int:pk>/update/', views.updatepage, name='updatepage'),
    path('<int:pk>/delete/', views.deletepage, name='deletepage'),
    path('<int:pk>/detai',views.detailpage, name='detailpage'),

    path('registerpage/',views.registerpage, name='registerpage'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logout/',views.logoutuser, name='logout'),
]