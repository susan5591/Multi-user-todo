from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("home/",views.home, name='home'),
    path('create/',views.create , name='create'),
    path('<int:pk>/update/', views.updatepage, name='updatepage'),
    path('<int:pk>/delete/', views.deletepage, name='deletepage'),
    path('<int:pk>/detail/',views.detailpage, name='detailpage'),
    path('change-status/<int:pk>/<str:status>/', views.change_todo, name='changetodo'),

    path('registerpage/',views.registerpage, name='registerpage'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logout/',views.logoutuser, name='logout'),
]