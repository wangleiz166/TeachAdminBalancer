from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='staffvModules_list'),
    path('add/', views.staffvModules_course_add, name='staffvModules_course_add'),
    path('edit/<int:courseId>', views.staffvModules_course_edit, name='staffvModules_course_edit'),
    path('delete/<int:courseId>', views.staffvModules_course_del, name='staffvModules_course_del'),

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
]