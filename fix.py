from employees_app.models import Employee

for emp in Employee.objects.all():
    emp.name = emp.name.encode('latin-1').decode('utf-8')
    emp.save()