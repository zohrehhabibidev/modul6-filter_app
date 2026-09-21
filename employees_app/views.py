from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    employees = Employee.objects.all()

    context = {
        "employees": employees,
    }

    return render(request, "employee_list.html", context)
