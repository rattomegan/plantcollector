from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  # 'about/' - About Route
  path('about/', views.about, name='about'),

  # 'plants/' - Plants Index Route
  path('plants/', views.plants_index, name='plants_index'),
]