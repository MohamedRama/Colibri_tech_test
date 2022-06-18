from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import F
from .forms import EmployeeForm
from .models import Employee
from .custom_filters import EmployeeFilter
from .utils import get_serialized_data, get_empoyee_by_id, get_paginator


def home(request):
    return render(request, "home.html")

def employee_all(request):
    employees = Employee.objects.all()

    filterset = EmployeeFilter(request.GET, queryset=employees)
    if filterset.is_valid():
        employees = filterset.qs

    order_by = request.GET.get('order_by', None)
    if order_by:
        employees = employees.order_by(F(order_by).asc(nulls_last=True))
        
    page_obj = get_paginator(request, employees)

    obj_serialize = employees if not page_obj else page_obj
    data = get_serialized_data(obj_serialize)
    return HttpResponse(data, content_type='application/json')

def employee_one(request, pk):
    employee = get_empoyee_by_id(pk)
    data = get_serialized_data([employee])
    return HttpResponse(data, content_type='application/json')

def employee_update(request, pk):
    employee = get_empoyee_by_id(pk)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee-one', pk=pk)

    context = {"form": form}
    return render(request, "update_emp.html", context)

def employee_delete(request, pk):
    employee = get_empoyee_by_id(pk)
    if request.method =="POST":
        employee.delete()
        return redirect('employee-all')
    
    data = get_serialized_data([employee])
    context = {"employee": data}
    return render(request, "delete_emp.html", context)
