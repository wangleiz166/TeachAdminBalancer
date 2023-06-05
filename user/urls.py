from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('edit/', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('logs/', views.logs, name='logs'),
    path('permission/', views.permission, name='permission'),
    path('login/', views.login, name='login'),
]