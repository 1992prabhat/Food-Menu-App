from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Item(models.Model):

	class MealType(models.TextChoices):
		VEG = 'Vegetarian', 'Vegetarian'
		NON_VEG = 'Non-Vegetarian', 'Non-Vegetarian'
		MIXED = 'Mixed', 'Mixed'
	item_name = models.CharField(max_length=200)
	item_price = models.DecimalField(max_digits=6, decimal_places=2)
	item_description = CKEditor5Field('Description', config_name='default')
	meal_type = models.CharField(max_length=20, choices=MealType.choices, default=MealType.MIXED)
	item_image = models.CharField(max_length=500, default='https://storage.googleapis.com/ds-builder-bucket/000_menu_placeholder.png')
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.item_name

	# class Meta:
	# 	db_table = 'items'
