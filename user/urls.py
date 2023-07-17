from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('edit/<int:userId>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('logs/', views.logs, name='logs'),
    path('permission/', views.permission, name='permission'),
    path('login/', views.login, name='login'),
    path('delete/<int:userId>', views.user_del, name='list'),
    path('logout/', views.logout, name='logout'),
]
