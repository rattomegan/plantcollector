from django.db import models

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

class Plant(models.Model):
  name = models.CharField(max_length=200)
  latin_name = models.CharField(max_length=200)
  date_acquired = models.DateField()

  def __str__(self):
    return self.name