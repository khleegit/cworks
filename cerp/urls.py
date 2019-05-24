from django.urls import path
from . import views


urlpatterns = [
	path('', views.login, name='login'),
    path('home/', views.base, name='home'),
    path('counsel/', views.counsel, name='counsel'),
]