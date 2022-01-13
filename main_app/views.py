from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Plant
from .forms import FeedingForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {'plants': plants })

def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  feeding_form = FeedingForm()
  return render(request, 'plants/detail.html', { 
    'plant': plant,
    'feeding_form': feeding_form
  })

class PlantCreate(CreateView):
  model = Plant 
  fields = '__all__'
  success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  fields = '__all__'

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'

def add_feeding(request, plant_id):
  # Create a ModelForm instance using the data in request.Post, which will be an object with all data from the form
  form = FeedingForm(request.POST)
  if form.is_valid():
    # this creates an in memory copy of the feeding that we can add properties to
    new_feeding = form.save(commit=False)
    new_feeding.plant_id = plant_id
    new_feeding.save()
  return redirect('plants_detail', plant_id=plant_id)
