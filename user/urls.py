from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('edit/', views.edit, name='edit'),
    path('add/', views.add, name='add'),
]