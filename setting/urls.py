from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='setting_list'),
    path('permission/<str:permissionName>', views.permission_edit, name='permission_edit'),
    path('menu/', views.menu_edit, name='menu_edit'),
    path('warn/',views.warn, name="warn"),
    path('login_warn/',views.login_warn, name="login_warn"),
    path('guide/',views.guide, name="guide"),
]