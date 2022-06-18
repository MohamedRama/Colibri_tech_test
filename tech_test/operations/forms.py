from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
 
    class Meta:
        model = Employee
        
        fields = [
            "first_name",
            "last_name",
            "email",
            "gender",
            "date_of_birth",
            "industry",
            "salary",
            "years_of_experience"
        ]
