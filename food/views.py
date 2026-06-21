from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .forms import ItemForm
from .models import Item


# Create your views here.

# List all the food items
def index(request):
	items = Item.objects.all()

	context = {'items': items}
	return render(request, "food/index.html", context)

class ItemListView(ListView):
	model = Item
	template_name = "food/index.html"
	context_object_name = "items"


# Show the detail of a food item
def detail(request, item_id):
	try:
		item = Item.objects.get(id=item_id)
		return render(request, "food/detail.html", {"item": item})
	except Item.DoesNotExist:
		return render(request, "food/404.html")


# Add a new food item
@login_required
def add_food(request):
	form = ItemForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect("food:index")
		else:
			return render(request, "food/add_food.html", {"form": form})
	else:
		return render(request, "food/add_food.html", {"form": form})

# Edit a food item
@login_required
def edit_food(request, item_id):
	try:
		item = Item.objects.get(id=item_id)
		form = ItemForm(request.POST or None, instance=item)
	except Item.DoesNotExist:
		return render(request, "food/404.html")
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect("food:index")
		else:
			return render(request, "food/edit_food.html", {"form": form})
	else:
		return render(request, "food/edit_food.html", {"form": form})


# Delete a food item
@login_required
def delete_food(request, item_id):
	try:
		item = Item.objects.get(id=item_id)
		item.delete()
		return redirect("food:index")
	except Item.DoesNotExist:
		return render(request, "food/404.html")
