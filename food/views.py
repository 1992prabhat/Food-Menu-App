from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ItemForm
from .models import Item
# from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# List all the food items
def index(request):
	items = Item.objects.all()

	context = {'items': items}
	return render(request, "food/index.html", context)

# class ItemListView(ListView):
# 	model = Item
# 	template_name = "food/index.html"
# 	context_object_name = "items"


# Show the detail of a food item
def detail(request, pk):
	try:
		item = Item.objects.get(pk=pk)
		return render(request, "food/detail.html", {"item": item})
	except Item.DoesNotExist:
		return render(request, "food/404.html")

# class ItemDetailView(DetailView):
# 	model = Item
# 	template_name = "food/detail.html"
# 	context_object_name = "item"

# Add a new food item
@login_required
def add_food(request):
	# Set the author to the current user
	form = ItemForm(request.POST or None)

	if request.method == "POST":
		if form.is_valid():
			item = form.save(commit=False)
			item.author = request.user
			item.save()
			return redirect("food:index")
		else:
			return render(request, "food/add_food.html", {"form": form})
	else:
		return render(request, "food/add_food.html", {"form": form})

# class ItemCreateView(LoginRequiredMixin, CreateView):
# 	model = Item
# 	form_class = ItemForm
# 	success_url = "/food/"
# 	template_name = "food/add_food.html"
# 	login_url = "users:login"



	# Edit a food item
@login_required
def edit_food(request, pk):
	# Check if the user is the author of the item
	author = request.user
	try:
		item = Item.objects.get(pk=pk)
		if item.author != author:
			return render(request, "food/403.html")
		else:
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

# class ItemUpdateView(LoginRequiredMixin, UpdateView):
# 	model = Item
# 	form_class = ItemForm
# 	success_url = "/food/"
# 	template_name = "food/edit_food.html"
# 	login_url = "users:login"

# Delete a food item
@login_required
def delete_food(request, pk):
	# Check if the user is the author of the item
	author = request.user
	try:
		item = Item.objects.get(pk=pk)
		if item.author != author:
			return render(request, "food/403.html")
		else:
			item.delete()
			return redirect("food:index")
	except Item.DoesNotExist:
		return render(request, "food/404.html")

# class ItemDeleteView(LoginRequiredMixin, DeleteView):
# 	model = Item
# 	success_url = "/food/"

def forbidden(request):
	return render(request, "food/403.html")

# def