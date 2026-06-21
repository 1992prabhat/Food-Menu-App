from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
		path('login/', views.login, name='login'),
		path('logout/', views.user_logout, name='logout'),
		path('my-profile/', views.my_profile, name='my_profile'),
		path('edit-profile/', views.edit_profile, name='edit_profile'),
	]
