from django import forms
from .models import Employee_details

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['first_name', 'last_name', 'position', 'department','experience', 'work_type'] 
