from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('detail/<int:staffId>/', views.staff_detail, name='staff_detail'),
    path('add/', views.staff_add, name='staff_add'),
    path('bulk_add/', views.staff_bulk_add, name='staff_bulk_add'),
    path('delete/<int:staffId>/', views.staff_delete, name='staff_delete'),
    path('update/<int:staffId>/', views.staff_update, name='staff_update'),
    path('totalwork/<int:staffId>/', views.totalwork_h5, name='totalwork_h5'),
    
]