from django.urls import path
from departments import views

urlpatterns = [
   path('', views.departments_index, name='departments'),
   path('<int:id>', views.department_display, name='departments.display'),
]
