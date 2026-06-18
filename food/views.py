from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
	items = Item.objects.all()
	return HttpResponse(items)

def add_food(request):
	return HttpResponse("<h1 style='text-align: center; color: lightblue;'>Add Food</h1>")