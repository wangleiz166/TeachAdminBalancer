from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('detail/', views.staff_detail, name='staff_detail'),
    path('add/', views.staff_add, name='staff_add'),
    path('bulk_add/', views.staff_bulk_add, name='staff_bulk_add'),
]