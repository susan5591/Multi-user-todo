from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    tasks = TODO.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request,'todo/list.html',context)