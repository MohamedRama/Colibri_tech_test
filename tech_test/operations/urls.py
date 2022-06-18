from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/all/', views.employee_all, name='employee-all'),
    path('employee/id/<int:pk>/', views.employee_one, name='employee-one'),
    path('employee/id/<int:pk>/update/', views.employee_update, name='employee-update'),
    path('employee/id/<int:pk>/delete/', views.employee_delete , name='employee-delete'),
]
