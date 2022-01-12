from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  # 'about/' - About Route
  path('about/', views.about, name='about'),

  # 'plants/' - Plants Index Route
  path('plants/', views.plants_index, name='plants_index'),

  # 'plants/<int:plant_id>/' - Plants Detail View
  path('plants/<int:plant_id>/', views.plants_detail, name='plants_detail')
]