from django.urls import path
from . import views

urlpatterns = [
    path('', views.total_work_list, name='total_work_list'),
     path('detail/', views.total_work_detail, name='total_work_detail'),
    path('add/', views.total_work_add, name='total_work_add'),
    path('bulk_add/', views.total_work_bulk_add, name='total_work_bulk_add'),
]