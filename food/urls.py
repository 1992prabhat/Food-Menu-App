from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
		path('<int:item_id>/', views.detail, name='detail'),
    path('add-food/', views.add_food, name='add_food'),
		path('<int:item_id>/edit-food/', views.edit_food, name='edit_food'),
		path('<int:item_id>/delete-food/', views.delete_food, name='delete_food'),
]