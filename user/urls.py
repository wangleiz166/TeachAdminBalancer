from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('edit/<int:userId>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('logs/', views.logs, name='logs'),
    path('permission/', views.permission, name='permission'),
    path('login/', views.login, name='login'),
<<<<<<< HEAD
    path('delete/<int:userId>', views.user_del, name='list'),
]
=======
    path('logout/', views.logout, name='logout'),
]
>>>>>>> 787883819c2ceeab661e092a289a41096bba4df3
