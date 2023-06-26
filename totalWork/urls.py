from django.urls import path
from . import views

urlpatterns = [
    path('', views.total_work_list, name='total_work_list'),
    # path('totalWork/', views.total_work_list, name='total_work_list'),
    path('adminRoles/', views.admin_roles, name='admin_roles'),
    path('overallCalcs/', views.overall_calcs, name='overall_calcs'),
    path('frozenModules/', views.frozen_modules, name='frozen_modules'),
]