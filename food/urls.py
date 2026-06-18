from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-food/', views.add_food),
]