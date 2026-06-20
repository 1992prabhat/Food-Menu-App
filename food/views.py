from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from .forms import ItemForm

# Create your views here.

# List all the food items
def index(request):
	items = Item.objects.all()

	context = {'items': items}
	return render(request, "food/index.html", context)

# Show the detail of a food item
def detail(request, item_id):
	try:
		item = Item.objects.get(id=item_id)
		return render(request, "food/detail.html", {"item": item})
	except Item.DoesNotExist:
		return render(request, "food/404.html")


# Add a new food item
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
def delete_food(request, item_id):
	try:
		item = Item.objects.get(id=item_id)
		item.delete()
		return redirect("food:index")
	except Item.DoesNotExist:
		return render(request, "food/404.html")
