from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    context={

    }
    return render(request,'index.html',context)
