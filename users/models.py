from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)
	avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

	def __str__(self):
		return f'{self.user.first_name} {self.user.last_name}'

	class Meta:
		verbose_name = 'User Profile'
		verbose_name_plural = 'User Profiles'
