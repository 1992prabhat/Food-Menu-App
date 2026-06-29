from django.db import models


class ItemQuerySet(models.QuerySet):
	def alive(self):
		return self.filter(is_deleted=False)

	def deleted(self):
		return self.filter(is_deleted=True)


class ItemManager(models.Manager):
	def cheap_items(self):
		return self.filter(item_price__lte=10)

	def expensive_items(self):
		return self.filter(item_price__gt=10)

	def search_items(self, keyword):
		return self.filter(item_name__icontains=keyword)


	def get_queryset(self):
		return ItemQuerySet(self.model, using=self._db)

	def get_alive_items(self):
		return self.get_queryset().alive()

	def get_deleted_items(self):
		return self.get_queryset().deleted()

	def get_all_items(self):
		return self.get_queryset()