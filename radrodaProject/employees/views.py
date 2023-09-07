from django.shortcuts import render
from django.http import HttpResponse
from employees.models import employee
from django.shortcuts import redirect
from django.urls import reverse
from employees.forms import employeeForm

# Create your views here.

def employees_index(request):
    emps = employee.get_all_emps()
    return render(request,'./employee/emp.html', context={'emps':emps})

def employee_delete (request, id ):
    emp = employee.get_emp(id)
    emp.delete()
    print (reverse('employees'))
    print ("here we are !!!")
    redirect_url =  reverse('employees')
    return redirect(redirect_url)

def employee_display(request,id):
    emp = employee.get_emp(id)
    return render(request,"./employee/display.html", context={'emp':emp})

def employee_create(request):
    print ("we are in create")
    if request.method == 'GET':
        form = employeeForm()
        return render(request,"employee/create.html", context={'form':form})

    else :
        print(request.POST)
        form = employeeForm(request.POST , request.FILES)
        if form.is_valid():
                form.save()
        redirect_url =  reverse('employees')
        return redirect(redirect_url)

def employee_edit(request , id ):
    emp = employee.get_emp(id)
    if request.method == 'GET':
        form = employeeForm(instance=emp)
        return render(request,"employee/edit.html", context={'form':form})

    else :
        print(request.POST)
        form = employeeForm(request.POST , request.FILES, instance=emp)
        if form.is_valid():
                form.save()
        redirect_url = reverse("employees.display", args=[id]) 
        return redirect(redirect_url)
