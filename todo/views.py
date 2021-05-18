from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .filters import WorkFilter

# Create your views here.

def registerpage(request):
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('loginpage')
            
    context={
        'form':form
    }
    return render(request,'todo/register.html',context)


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,'Username or password is incorrect')
    context = {}
    return render(request,'todo/login.html',context)


def logoutuser(request):
    logout(request)
    return redirect('loginpage')


def home(request):
    if request.user.is_authenticated:
        user = request.user
        tasks = TODO.objects.filter(user = user).order_by('-status','-priority')
        myFilter = WorkFilter(request.GET, queryset = tasks)
        tasks = myFilter.qs
        context = {
            'tasks':tasks,
            'myFilter':myFilter  
        }
        return render(request,'todo/list.html',context)


def create(request):
    form = TODOForm()
    if request.method == 'POST':
        user = request.user
        form = TODOForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home') 
    context ={
        'form':form
        }
    return render(request,'todo/create.html',context)


def detailpage(request,pk):
    title = TODO.objects.get(id=pk)
    context = {
        'title':title
    }
    return render(request,'todo/details.html',context)


def updatepage(request,pk):
    title = TODO.objects.get(id=pk)
    form = TODOForm(instance = title)
    if request.method == "POST":
        form = TODOForm(request.POST, instance=title)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request,'todo/update.html',context)


def deletepage(request,pk):
    title = TODO.objects.get(id=pk)
    form = TODOForm()
    if request.method=='POST':
        title.delete()
        return redirect('home')
    context={
        'title':title
    }
    return render(request,'todo/delete.html',context)
