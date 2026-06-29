from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = CKEditor5Field('Description', default='', config_name='default')
	website = models.URLField(blank=True, null=True)
	avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

	def __str__(self):
		return f'{self.user.first_name} {self.user.last_name}'

	class Meta:
		verbose_name = 'User Profile'
		verbose_name_plural = 'User Profiles'
