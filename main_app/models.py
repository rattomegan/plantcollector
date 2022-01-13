from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from datetime import date

# Create your models here.
# class Plant():
#   def __init__(self, name, latin_name):
#     self.name = name
#     self.latin_name = latin_name
  
# plants = [
#   Plant('Monstera', 'Monstera deliciosa'),
#   Plant('Rubber Tree', 'Ficus elastica'),
#   Plant('Fiddle Leaf Fig', 'Ficus lyrata')
# ]

TOXICITY = (
  ('Severe', 'Severly toxic'),
  ('Mild', 'Mildy toxic'),
  ('None', 'No or low toxicity')
)

class Watering(models.Model):
  date = models.DateField('Watering Date')

  def __str__(self):
    return f'Watering on {self.date}'

  def get_absolute_url(self):
    return reverse('waterings_detail', kwargs={'pk': self.id})

class Plant(models.Model):
  name = models.CharField(max_length=200)
  latin_name = models.CharField(max_length=200)
  date_acquired = models.DateField()
  # Add relationship to Watering model
  waterings = models.ManyToManyField(Watering)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('plants_detail', kwargs={'plant_id': self.id})

  def fed_for_summer(self):
    year = date.today().year
    return self.feeding_set.filter(date__range=[f'{year}-06-21', f'{year}-09-22']).count() >= 13

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  type = CharField(
    max_length=200,
    default='Plant Food',
    editable=True
  )
  
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.type} on {self.date}'

  class Meta:
    ordering = ['-date']


class Care(models.Model):
  plant = models.OneToOneField(
    Plant, 
    on_delete=models.CASCADE,
    primary_key=True,
  )
  light = models.TextField(max_length=300)
  water = models.TextField(max_length=300)
  instructions = models.TextField(
    max_length=400,
    default='Feed every two weeks in growing season',
    editable=True
  )
  toxicity = models.CharField(
    max_length=6,
    choices=TOXICITY,
    default=TOXICITY[0][0]
  )

  def __str__(self):
    return f'{self.name} is {self.get_toxicity_display()}'