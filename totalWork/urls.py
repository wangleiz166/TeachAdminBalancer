from django.urls import path
from . import views

urlpatterns = [
    path('', views.total_work_list, name='total_work_list'),
]