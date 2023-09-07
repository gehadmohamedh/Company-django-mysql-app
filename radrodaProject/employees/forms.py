from django import forms 
from employees.models import employee

class employeeForm (forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'

