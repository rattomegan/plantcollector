from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  # 'about/' - About Route
  path('about/', views.about, name='about'),

  # 'plants/' - Plants Index Route
  path('plants/', views.plants_index, name='plants_index'),

  # 'plants/<int:plant_id>/' - Plants Detail View
  path('plants/<int:plant_id>/', views.plants_detail, name='plants_detail'),

  # 'plants/create/' - Plants Create Route
  path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),

  # 'plants/<int:pk>/update/' - Update Plants Route
  path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),

  # 'plants/<int:pk>/delete/' - Delete Plants Route
  path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),

  path('plants/<int:plant_id>/add_feeding/', views.add_feeding, name='add_feeding'),

  path('plants/<int:plant_id>/assoc_watering/<int:watering_id>/', views.assoc_watering, name='assoc_watering'),
  path('plants/<int:plant_id>/unassoc_watering/<int:watering_id>/', views.unassoc_watering, name='unassoc_watering'),


  path('waterings/', views.WateringList.as_view(), name='waterings_index'),
  path('waterings/<int:pk>/', views.WateringDetail.as_view(), name='waterings_detail'),
  path('waterings/create/', views.WateringCreate.as_view(), name='waterings_create'),
  path('waterings/<int:pk>/update/', views.WateringUpdate.as_view(), name='waterings_update'),
  path('waterings/<int:pk>/delete/', views.WateringDelete.as_view(), name='waterings_delete'),
]

