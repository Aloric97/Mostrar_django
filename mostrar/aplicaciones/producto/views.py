from django.shortcuts import render
from .models import producto

# Create your views here.

def home(request):
    productos= producto.objects.all()
    return render(request,'index.html', {"productos":productos})