from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Plant, Watering
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
  # find all waterings not associated with this plant then pass it down as a 'waterings' variable
  waterings_plant_didnt_get = Watering.objects.exclude(id__in=plant.waterings.all().values_list('id'))
  return render(request, 'plants/detail.html', { 
    'plant': plant,
    'feeding_form': feeding_form,
    'waterings': waterings_plant_didnt_get
  })

class PlantCreate(CreateView):
  model = Plant 
  fields = ['name', 'latin_name', 'date_acquired']
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

class WateringList(ListView):
  model = Watering

class WateringDetail(DetailView):
  model = Watering

class WateringCreate(CreateView):
  model = Watering
  fields = '__all__'

class WateringUpdate(UpdateView):
  model = Watering
  fields = '__all__'

class WateringDelete(DeleteView):
  model = Watering
  success_url = '/waterings/'

def assoc_watering(request, plant_id, watering_id):
  Plant.objects.get(id=plant_id).waterings.add(watering_id)
  return redirect('plants_detail', plant_id=plant_id)

def remove_watering(request, plant_id, watering_id):
  Plant.objects.get(id=plant_id).waterings.remove(watering_id)
  return redirect('plants_detail', plant_id=plant_id)