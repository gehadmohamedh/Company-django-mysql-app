from django.urls import path
from employees import views

urlpatterns = [
   path('', views.employees_index, name='employees'),
   path('<int:id>/delete' , views.employee_delete ,name='employees.delete'),
   path('<int:id>/display' , views.employee_display ,name='employees.display'),
   path('create' , views.employee_create ,name ='employees.create' ),
   path('<int:id>/edit' , views.employee_edit ,name ='employees.edit' )
]
