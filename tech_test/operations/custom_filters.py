import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'id': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'email': ['icontains'],
            'gender': ['exact'],
            'date_of_birth': ['icontains'],
            'industry': ['icontains'],
            'salary': ['exact', 'lt', 'gt'],
            'years_of_experience': ['exact', 'lt', 'gt'],   
        }
