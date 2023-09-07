from django.shortcuts import render
from departments.models import department
from employees.models import employee

# Create your views here.

def departments_index(request):
    deps = department.get_all_deps()
    print(deps)
    return render(request,'./departments/departments.html', context={'deps':deps})

def department_display(request,id):
    dep = department.get_dep(id)
    emps= employee.objects.filter(dept=id)
    return render(request,"./departments/display.html", context={'dep':dep , 'emps':emps})
