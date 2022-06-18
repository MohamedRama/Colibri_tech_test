from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core import serializers
from .models import Employee


def get_paginator(request, employees):
    paginate_by = request.GET.get('paginate_by', None)
    page_obj = None
    if paginate_by:
        paginator = Paginator(employees, paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return page_obj

def get_empoyee_by_id(employee_id):
    return get_object_or_404(Employee, id=employee_id)

def get_serialized_data(obj_data):
    return serializers.serialize('json', obj_data)
