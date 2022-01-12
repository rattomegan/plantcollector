from django.shortcuts import render
from .models import plants as plants


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  return render(request, 'plants/index.html', { 'plants': plants })