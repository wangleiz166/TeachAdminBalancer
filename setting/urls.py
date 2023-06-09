from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('permission/', views.permission_edit, name='permission_edit'),
    path('menu/', views.menu_edit, name='menu_edit'),
]