from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):
    employees = Employee.objects.all()
    high_earners = Employee.objects.filter(salary__gt=3000)
    high_earners_count = Employee.objects.filter(salary__gte=5000).count()
    sales_employees = Employee.objects.filter(department__name="Sales")
    avg_salary = sales_employees.aggregate(Avg("salary"))
    avg_salary = round(avg_salary["salary__avg"], 2)
    hired_employees = Employee.objects.filter(hire_date__lt=date(2022, 1, 1)).exclude(
        department__name="HR"
    )

    return render(
        request,
        "employee_list.html",
        {
            "employees": employees,
            "high_earners": high_earners,
            "high_earners_count": high_earners_count,
            "avg_salary": avg_salary,
            "hired_employees": hired_employees,
        },
    )
