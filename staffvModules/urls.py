from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='staffvModules_list'),
    path('detail/', views.detail, name='detail'),
]