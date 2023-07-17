from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='staffvModules_list'),
    path('detail/<int:staffId>', views.detail, name='detail'),
    path('add/', views.staffvModules_course_add, name='staffvModules_course_add'),
    path('edit/<int:courseId>', views.staffvModules_course_edit, name='staffvModules_course_edit'),
    path('delete/<int:courseId>', views.staffvModules_course_del, name='staffvModules_course_del'),
    path('stafflist/<str:name>/<str:type>', views.staff_list, name='staff_list'),
    path('hstotal', views.hs_total_list, name='hs_total_list'),
    
  
    path('project/', views.project_list, name='staffvModules_project_list'),
    path('project/add/', views.staffvModules_project_add, name='staffvModules_project_add'),
    path('project/edit/<int:projectId>', views.staffvModules_project_edit, name='staffvModules_project_edit'),
    path('project/delete/<int:projectId>', views.staffvModules_project_del, name='staffvModules_project_del'),

    path('adminRole/', views.adminrole_list, name='staffvModules_adminrole_list'),
    path('adminRole/add/', views.staffvModules_adminrole_add, name='staffvModules_adminrole_add'),
    path('adminRole/edit/<int:adminroleId>', views.staffvModules_adminrole_edit, name='staffvModules_adminrole_edit'),
    path('adminRole/delete/<int:adminroleId>', views.staffvModules_adminrole_del, name='staffvModules_adminrole_del'),

    path('schoolRole/', views.schoolrole_list, name='staffvModules_schoolrole_list'),
    path('schoolRole/add/', views.staffvModules_schoolrole_add, name='staffvModules_schoolrole_add'),
    path('schoolRole/edit/<int:schoolroleId>', views.staffvModules_schoolrole_edit, name='staffvModules_schoolrole_edit'),
    path('schoolRole/delete/<int:schoolroleId>', views.staffvModules_schoolrole_del, name='staffvModules_schoolrole_del'),

    path('uniRole/', views.unirole_list, name='staffvModules_unirole_list'),
    path('uniRole/add/', views.staffvModules_unirole_add, name='staffvModules_unirole_add'),
    path('uniRole/edit/<int:uniroleId>', views.staffvModules_unirole_edit, name='staffvModules_unirole_edit'),
    path('uniRole/delete/<int:uniroleId>', views.staffvModules_unirole_del, name='staffvModules_unirole_del'),


    path('full/', views.full_list, name='staffvModules_full_course_list'),
    path('full/project/', views.full_list, {'category': 'project'}, name='staffvModules_full_project_list'),
    path('full/adminRole/', views.full_list, {'category': 'adminrole'}, name='staffvModules_full_adminrole_list'),
    path('full/schoolRole/', views.full_list, {'category': 'schoolrole'}, name='staffvModules_full_schoolrole_list'),
    path('full/uniRole/', views.full_list, {'category': 'unirole'}, name='staffvModules_full_unirole_list'),

    path('full/edit/<str:type>', views.full_edit, name='staffvModules_full_edit'),
]