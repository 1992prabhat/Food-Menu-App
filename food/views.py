from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
	items = Item.objects.all()

	context = {'items': items}
	return render(request, "food/index.html", context)

def detail(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	return render(request, "food/detail.html", {"item": item})

def add_food(request):
	return HttpResponse("<h1 style='text-align: center; color: lightblue;'>Add Food</h1>")