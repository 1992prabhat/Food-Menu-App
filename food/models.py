from django.db import models

# Create your models here.
class Item(models.Model):
	item_name = models.CharField(max_length=200)
	item_price = models.DecimalField(max_digits=6, decimal_places=2)
	item_description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.item_name

	# class Meta:
	# 	db_table = 'items'