from django.urls import path
from . import views

urlpatterns = [
    path('', views.total_work_list, name='total_work_list'),
    # path('totalWork/', views.total_work_list, name='total_work_list'),
    path('adminRoles/', views.admin_roles, name='admin_roles'),
    path('overallCalcs/', views.overall_calcs, name='overall_calcs'),
    path('frozenModules/', views.frozen_modules, name='frozen_modules'),
    path('download_total_work/', views.export_total_work_to_csv, name='download_total_work'),
    path('download_admin_roles/', views.download_admin_roles, name='download_admin_roles'),
    path('download_overall_calcs/', views.download_overall_calcs, name='download_overall_calcs'),
]