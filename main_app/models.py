from django.db import models

# Create your models here.
class Plant():
  def __init__(self, name, latin_name):
    self.name = name
    self.latin_name = latin_name
  

plants = [
  Plant('Monstera', 'Monstera deliciosa'),
  Plant('Rubber Tree', 'Ficus elastica'),
  Plant('Fiddle Leaf Fig', 'Ficus lyrata')
]