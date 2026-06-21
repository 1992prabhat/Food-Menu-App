from django import forms
from .models import Item
from django.core.exceptions import ValidationError
import re

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['item_name', 'item_price', 'item_description', 'item_image']

		widgets = {
			'item_name': forms.TextInput(attrs={
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
			}),
			'item_description': forms.Textarea(attrs={
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none',
				'rows': 4
			}),
			'item_price': forms.NumberInput(attrs={
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
			}),
			'item_image': forms.URLInput(attrs={
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
			}),
		}

	def clean_item_name(self):
		item_name = self.cleaned_data['item_name']
		if item_name.isdigit():
				raise ValidationError("Item name cannot be a number.")
		if item_name.isspace():
				raise ValidationError("Item name cannot be empty.")
		if not re.match(r'^[a-zA-Z0-9\s]+$', item_name):
				raise ValidationError("Item name can only contain letters, numbers, and spaces.")
		return item_name

	def clean_item_price(self):
		item_price = self.cleaned_data['item_price']
		if item_price <= 0:
				raise ValidationError("Item price must be greater than 0.")
		return item_price

	def clean_item_description(self):
		item_description = self.cleaned_data['item_description']
		if not item_description.strip():
			raise ValidationError("Item description cannot be empty.")
		if len(item_description) < 10:
			raise ValidationError("Item description must be at least 10 characters long.")
		return item_description

	def clean_item_image(self):
		item_image = self.cleaned_data['item_image']
		if not item_image.startswith('http'):
			raise ValidationError("Item image must be a valid URL.")
		return item_image

