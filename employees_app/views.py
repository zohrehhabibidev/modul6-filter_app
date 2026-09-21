from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    employees = Employee.objects.all()
    high_earners = Employee.objects.filter(salary__gt=3000)
    employees_5000 = Employee.objects.filter(salary__gte=5000).count()
    sales_average = Employee.objects.filter(
        department__name="Sales"
    ).aggregate(
        avg_salary=Avg("salary")
    )["avg_salary"]

    context = {
        "employees": employees,
        "high_earners": high_earners,
        "employees_5000": employees_5000,
        "sales_average": sales_average,
    }

    return render(request, "employee_list.html", context)
