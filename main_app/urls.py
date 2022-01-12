from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  # 'about/' - About Route
  path('about/', views.about, name='about')
]